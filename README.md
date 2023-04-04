Interface web para controle da comunidade do Litpeg

Caminho que utilizo para ativar a máquina virtual: 
1) python -m venv venv
2) venv\Scripts\activate

Bibliotecas instaladas:

Digita "pip freeze" no terminal que mostra as bibliotecas instaladas. "pip freeze > requirements.txt" transfere as bibliotecas instaladas para o arquivo "requirements.txt". Lembrando que sempre que baixar alguma biblioteca nova, é necessário inserir o comando acima novamente. 
"pip install -r requirements.txt" lê o arquivo e faz o dowload de todas as bibliotecas utilizadas para a sua máquina.


LINKS:

Interface inspirada no projeto do curso abaixo:
https://www.youtube.com/watch?v=oORKCL7MwSo&list=PLV5pQ5hJ6r7OZjjLFWR8Ag18ZxqBikktz&index=1

Conexão do Django com o Banco de dados PostgreSql:
https://www.horadecodar.com.br/2019/01/24/integrando-django-com-postegresql-windows-e-linux/

Fazer buscas no banco de dados:
https://www.youtube.com/watch?v=MQuinp8_OWU

Fazer Dashboard estatístico com CHART.JS:
https://www.youtube.com/watch?v=HozwGeEiXIk

Fazer Deploy com Apache:
https://www.youtube.com/watch?v=frEjX1DNSpc

Resolvendo o problema com a execução do "mod_wsgi-express module-config" do seguinte ERROR: 

BINDIR = 'C:\xampp\apache/bin'
^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-4: truncated \xXX escape

Instale o xampp na raiz do computador (C:) juntamente com o dowloado do Apache também na raiz conforme indicado no vídeo anterior do deploy com o apache.
A partir disso, com base nesses dois sites também:
https://github.com/GrahamDumpleton/mod_wsgi/issues/685
https://stackoverflow.com/questions/64476554/mod-wsgi-express-module-config-issue

Foi necessário fazer os seguintes passos no terminal CMD:
1) pip uninstall mod_wsgi
2) set "MOD_WSGI_APACHE_ROOTDIR=C:/xampp/Apache"
3) pip install --no-cache-dir mod_wsgi
4) Execute o "mod_wsgi-express module-config" e verifique se funcionou.
5) caso funcione, volte ao vídeo e de seguimento ao passo a passo.

Nas configurações do arquivo httpd.conf do apache insira os caminhos dos arquivos exibidos após a execução do "mod_wsgi-express module-config" conforme explicado no vídeo.
O que vai resultar o seguinte modelo:

""" -> Copie sem as aspas

ServerName 150.161.138.12:80

# Django Project
LoadFile "c:/python311/python311.dll"
LoadModule wsgi_module "c:/python311/lib/site-packages/mod_wsgi/server/mod_wsgi.cp311-win_amd64.pyd"
WSGIPythonHome "c:/python311"
WSGIScriptAlias / "C:/Users/Thiago_Botelho/projeto_litpeg/project/wsgi.py"
WSGIPythonPath C:\Users\Thiago_Botelho\projeto_litpeg;C:\Python311\DLLs;C:\Python311\Lib\site-packages

<Directory "C:/Users/Thiago_Botelho/projeto_litpeg/project/">
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>

Alias /static "C:/Users/Thiago_Botelho/projeto_litpeg/staticfiles/"
<Directory "C:/Users/Thiago_Botelho/projeto_litpeg/staticfiles/">
    Require all granted
</Directory>
""" -> Copie sem as aspas

Obs: No caminho do alias do static, verifique qual é o caminho da pasta dos arquivos estáticos executando o "python manage.py collectstatic", onde vai mostrar o caminho em que os arquivos estáticos foram salvos.
Ex: 
C:\Users\Thiago_Botelho\projeto_litpeg> python manage.py collectstatic

You have requested to collect static files at the destination
location as specified in your settings:

    C:\Users\Thiago_Botelho\projeto_litpeg\staticfiles
    
Com o caminho retornado, altere as barras de \ para / e cole no trecho "Alias /static" e no trecho "<Directory" das configurações mostradas acima do httpd.conf do apache.

Com tudo finalizado, abra o CMD como administrador e digite "cd .." até chegar na raiz do computador (C:\>), após isso, digite "cd Apache24" para entrar na pasta do apache.
Com isso há os seguintes comandos a serem inseridos no C:\Apache24>:
- Inicializar o apache: bin\httpd.exe -k start
- Reiniciar o apache: bin\httpd.exe -k restart
- Interromper o apache: bin\httpd.exe -k stop

Após rodar o apache, se não aparecer o site, verifique o log de erros e se aparecer algo do tipo informando que tal biblioteca não está instalada e você instalar no projeto e começar a aparecer vários erros desse tipo em sequência, é sinal de que as bibliotecas não foram instaladas direito, portanto execute o comando "pip uninstall -r requirements.txt" e depois o "pip install -r requirements.txt" para reinstalar tudo novamente. Após esses passos verifique se normalizou a situação.
Obs: É válido depois de instalar e reinstalar, reiniciar o computador.


Para acessar as configurações do Recaptcha do Gooogle, basta acessar o seguinte link utilizando a conta de TI do Litepg:
https://www.google.com/recaptcha/admin/site/625057727/settings
