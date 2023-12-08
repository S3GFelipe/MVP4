Instruções de uso do Back-End do MVP4 do aluno Felipe Florêncio de Andrade


# Passo a passo via terminal de como acessar a documentação  da API 

1. Criação do ambiente virtual

```
python -m venv env
.\env\Scripts\Activate
```

2. Instalação das bibliotecas necessárias para o funcionamento da API no diretório raiz

```
(env)$ pip install -r requirements.txt
```

3. Execução e reinicialização da API

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

4. Acessar a URL referente a documentação

Acesso da documentação via [http://localhost:5000/#/](http://localhost:5000/#/) no navegador 


