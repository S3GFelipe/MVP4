Instruções de uso do Back-End do MVP3 do aluno Felipe Florêncio de Andrade

Passo a passo via terminal de como acessar a documentação da API
Criação do ambiente virtual
python -m venv env
.\env\Scripts\Activate
Instalação das bibliotecas necessárias para o funcionamento da API no diretório raiz
(env)$ pip install -r requirements.txt
Execução e reinicialização da API
(env)$ flask run --host 0.0.0.0 --port 5000
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
Acessar a URL referente a documentação
Acesso da documentação via http://localhost:5000/#/ no navegador

Sobre o Docker

Como executar através do Docker Certifique-se de ter o Docker instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile no terminal e seus arquivos de aplicação e Execute como administrador o seguinte comando para construir a imagem Docker:

$ docker build -t api .
Uma vez criada a imagem, para executar o container basta executar, como administrador, seguinte o comando:

$ docker run -d -p 5000:5000 api
Uma vez executando, para acessar a API, basta abrir no navegador:

http://localhost:5000/#/ 
Alguns comandos úteis do Docker

Para verificar se a imagem foi criada, você pode executar o seguinte comando:

$ docker images
Caso queira remover uma imagem, basta executar o comando:

$ docker rmi <IMAGE ID>
Substituindo o IMAGE ID pelo código da imagem

Para verificar se o container esta em execução você pode executar o seguinte comando:

$ docker container ls --all
