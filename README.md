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


# Para acessar o front-end, basta executar o arquivo index.html para abrir a interface web.


# Sobre o Notebook para treinamento do modelo

O arquivo nomeado MVP4_FELIPE_ANDRADE_Final.ipynb foi gerado através do Google Colab

# Sobre o Dataset escolhido

Este conjunto de dados sintético é modelado a partir de uma fresadora existente e consiste em 10.000 pontos de dados armazenados.

Link de acesso: https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020

Não foram utilizadas todas as classes do dataset por finalidades didaticas.

# Sobre os parâmetros do Dataset

temperatura do ar [Convertida de K para °C]: gerada usando um processo de passeio aleatório posteriormente normalizado para um desvio padrão de 2 K em torno de 300 K
temperatura do processo [Convertida de K para °C]: gerada usando um processo de passeio aleatório normalizado para um desvio padrão de 1 K, adicionado à temperatura do ar mais 10 K.
velocidade de rotação [rpm]: calculada a partir de uma potência de 2860 W, sobreposta a um ruído normalmente distribuído
torque [Nm]: os valores de torque são normalmente distribuídos em torno de 40 Nm com SD = 10 Nm e sem valores negativos.
desgaste da ferramenta [min]: As variantes de qualidade H/M/L adicionam 5/3/2 minutos de desgaste da ferramenta à ferramenta utilizada no processo.



