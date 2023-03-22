from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from main.forms import NovoUsuarioForm
import psycopg2
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes 
import os
from django.core.cache import cache
from django.views.decorators.cache import never_cache
from datetime import date, datetime

def register(request):
    form = NovoUsuarioForm()
    if request.method == "POST":
        form = NovoUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login(request, user) -> para criar o usuário e logar logo depois nessa conta
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('/laboratorio/')
    context = {'form': form}
    return render(request, template_name='main/register.html', context=context)


def alterarSenha(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/laboratorio/')
        messages.error(request, "Falha na alteração da senha do usuário.")
    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, template_name='main/alterar_senha.html', context=context)

# Criar relatório para baixar lista de membros do Litpeg compatível com a catraca
# Dica do chat-gpt para não ter cache "@never_cache"
@never_cache
def baixar_lista(request):
  if request.method == "POST":
    # Quando clica no botão confirmar, executa o que está aqui dentro.
    cache.clear()
    conn = psycopg2.connect(dbname="membros_litpeg", user="postgres", password="@litpegti22")
    cur = conn.cursor()
    cur.execute("""SELECT numero_cracha, nome_completo FROM public.laboratorio_pessoa
                    WHERE status = 'Ativo'
                    ORDER BY nome_completo ASC  """)
    resultado = cur.fetchall()

    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d_%m_%Y_%Hh%M:%S')
    print(data_e_hora_em_texto)

    # SALVANDO NO TXT
    # Regras para colocar os núm do crachás e nomes dos membros:
    # with open(f'wlistas_nomes_baixadas/lista_nomes_{data_e_hora_em_texto}.txt', 'w') as arquivo:
    primeiro_ciclo = 0
    with open(f'C:\\Users\\Thiago_Botelho\\projeto_litpeg\\lista_nomes_{data_e_hora_em_texto}.txt', 'w') as arquivo:
      print("Era pra criar um novo arquivo")
      for res in resultado:
        codigo_acesso = "00010"
        num_cracha = str(res[0])
        nome_completo = str(res[1])

        # Tratamento para impedir nomes com mais de 40 caracteres
        while len(nome_completo) > 40:
          nome_novo = nome_completo.split()
          del(nome_novo[-1])
          nome_completo = " ".join(nome_novo)

        # Para saber a quantidade de espaços que precisa inserir:
        conta_cracha = 16 - len(num_cracha) 
        conta_nome = 40 - len(nome_completo)
        if primeiro_ciclo == 0:
          arquivo.write(num_cracha + (' ' * conta_cracha) + nome_completo + (' ' * conta_nome) + codigo_acesso)
          primeiro_ciclo = 1
        else:
          arquivo.write('\n' + num_cracha + (' ' * conta_cracha) + nome_completo + (' ' * conta_nome) + codigo_acesso)
      
      # conn.close()

    caminho = os.path.join("C:", "Users", "Thiago_Botelho", "projeto_litpeg", "lista_nomes.txt")

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #filename = caminho
    filename = f'C:\\Users\\Thiago_Botelho\\projeto_litpeg\\lista_nomes_{data_e_hora_em_texto}.txt'
    #filename = f'\\lista_nomes.txt'
    ##filepath = base_dir + filename
    ##thefile = filepath
    thefile = filename
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile, 'rb'), chunk_size), content_type=mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachement;filename=%s" % filename
    return response

  return render(request, 'main/baixar_arquivo.html')

# Criar aba de estatísticas dos membros
def estatisticas(request):
    if request.method == "GET":
        return render(request, 'main/estatisticas.html')


def total_func_ativo(request):
    if request.method == "GET":

        conn = psycopg2.connect(dbname="membros_litpeg", user="postgres", password="@litpegti22")
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(nome_completo) FROM public.laboratorio_pessoa
                        WHERE status = 'Ativo'  """)
        resultado = cur.fetchone()
        total = resultado[0]


        return JsonResponse({'total': total})


def total_func_inativo(request):
    if request.method == "GET":

        conn = psycopg2.connect(dbname="membros_litpeg", user="postgres", password="@litpegti22")
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(nome_completo) FROM public.laboratorio_pessoa
                        WHERE status = 'Inativo'  """)
        resultado = cur.fetchone()
        total = resultado[0]


        return JsonResponse({'total': total})


def divisao_genero(request):
    if request.method == "GET":
        
        data = []
        labels = []
        conn = psycopg2.connect(dbname="membros_litpeg", user="postgres", password="@litpegti22")
        cur = conn.cursor()
        cur.execute("""SELECT genero, COUNT(*) AS total_genero
                        FROM public.laboratorio_pessoa
                        GROUP BY genero  """)
        resultado = cur.fetchall()
        
        for res in resultado:
            labels.append(res[0])
            data.append(res[1])

        print(labels)
        print(data)
        return JsonResponse({'data': data, 'labels': labels})


def divisao_bolsa(request):
    if request.method == "GET":
        
        data = []
        labels = []
        conn = psycopg2.connect(dbname="membros_litpeg", user="postgres", password="@litpegti22")
        cur = conn.cursor()
        cur.execute("""SELECT bolsista, COUNT(*) AS quantidade
                        FROM public.laboratorio_pessoa
                        GROUP BY bolsista  """)
        resultado = cur.fetchall()
        for res in resultado:
            labels.append(res[0])
            data.append(res[1])

        return JsonResponse({'data': data, 'labels': labels}, json_dumps_params={'ensure_ascii': False})
        # O json_dumps_params={'ensure_ascii': False} serve para corrigir a acentuação.


def divisao_funcao(request):
    if request.method == "GET":
        
        data = []
        labels = []
        conn = psycopg2.connect(dbname="membros_litpeg", user="postgres", password="@litpegti22")
        cur = conn.cursor()
        cur.execute("""SELECT funcao, COUNT(*) AS quantidade
                        FROM public.laboratorio_pessoa
                        GROUP BY funcao  """)
        resultado = cur.fetchall()
        for res in resultado:
            labels.append(res[0])
            data.append(res[1])


        return JsonResponse({'data': data, 'labels': labels}, json_dumps_params={'ensure_ascii': False})
        # O json_dumps_params={'ensure_ascii': False} serve para corrigir a acentuação.


def qtd_membros_por_lab(request):
    if request.method == "GET":
        
        data = []
        labels = []
        conn = psycopg2.connect(dbname="membros_litpeg", user="postgres", password="@litpegti22")
        cur = conn.cursor()
        cur.execute("""SELECT L.nome_lab, COUNT(P.nome_completo) AS quantidade
                        FROM public.laboratorio_laboratorio as L
                        JOIN public.laboratorio_pessoa as P
                        ON L.id = P.laboratorio_id
                        GROUP BY L.nome_lab  """)
        resultado = cur.fetchall()
        for res in resultado:
          # Pega a parte final do nome do laboratório para encurtar
          novo = str(res[0]).split()
          labels.append(novo[-1])
          data.append(res[1])


        return JsonResponse({'data': data, 'labels': labels}, json_dumps_params={'ensure_ascii': False})
        # O json_dumps_params={'ensure_ascii': False} serve para corrigir a acentuação.