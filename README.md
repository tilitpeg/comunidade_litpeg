Interface web para controle da comunidade do Litpeg

Caminho que utilizo para ativar a máquina virtual: 
1) python -m venv venv
2) venv\Scripts\activate

Bibliotecas instaladas:

Digita "pip freeze" no terminal que mostra as bibliotecas instaladas. "pip freeze > requirements.txt" transfere as bibliotecas instaladas para o arquivo "requirements.txt". Lembrando que sempre que baixar alguma biblioteca nova, é necessário inserir o comando acima novamente. "pip install -r requirements.txt" lê o arquivo e faz o dowload de todas as bibliotecas utilizadas para a sua máquina.


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


