from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from flask import request 
import numpy as np
import pickle, joblib
from sqlalchemy.exc import IntegrityError

from model import Session, Equipamento, Model
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
equipamento_tag = Tag(name="Equipamento", description="Adição, visualização, remoção e predição de manutenção preventiva de equipamentos")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de equipamentos
@app.get('/equipamentos', tags=[equipamento_tag],
         responses={"200": EquipamentoViewSchema, "404": ErrorSchema})
def get_equipamentos():
    """Lista todos os equipamentos cadastrados na base
    Retorna uma lista de equipamentos cadastrados na base.
    
    Args:
        nome (str): nome do equipamento
        
    Returns:
        list: lista de equipamentos cadastrados na base
    """
    session = Session()
    
    # Buscando todos os equipamentos
    equipamentos = session.query(Equipamento).all()
    
    if not equipamentos:
        logger.warning("Não há equipamentos cadastrados na base :/")
        return {"message": "Não há equipamentos cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d equipamentos econtrados" % len(equipamentos))
        return apresenta_equipamentos(equipamentos), 200

# Rota de adição de equipamento
@app.post('/equipamento', tags=[equipamento_tag],
          responses={"200": EquipamentoViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: EquipamentoSchema):
    """Adiciona um novo equipamento à base de dados
    Retorna uma representação dos equipamentos e diagnósticos associados.
    
    Args:
        name (str): nome do equipamento
        temp: temperatura do ar
        proc: temperatura do processo
        vel: velocidade de rotação
        tor: toque
        des: desgaste da ferramenta
        outcome: diagnóstico
        data_insercao: data de quando o equipamento foi inserido à base
        
    Returns:
        dict: representação do equipamento e diagnóstico associado
    """
    
    # Carregando modelo
    ml_path = 'ml_model/classificador.pkl'
    scaler = joblib.load('ml_model/scaler.joblib')
    modelo = Model.carrega_modelo(ml_path, scaler)
    
    equipamento = Equipamento(
        name=form.name.strip(),
        temp=form.temp,
        proc=form.proc,
        vel=form.vel,
        tor=form.tor,
        des=form.des,
        outcome=Model.preditor(modelo, form)
    )
    logger.debug(f"Adicionando produto de nome: '{equipamento.name}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se equipamento já existe na base
        if session.query(Equipamento).filter(Equipamento.name == form.name).first():
            error_msg = "Equipamento já existente na base :/"
            logger.warning(f"Erro ao adicionar equipamento '{equipamento.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando equipamento
        session.add(equipamento)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado equipamento de nome: '{equipamento.name}'")
        return apresenta_equipamento(equipamento), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar equipamento '{equipamento.name}', {error_msg}")
        return {"message": error_msg}, 400
 
# Métodos baseados em nome
# Rota de busca de equipamento por nome
@app.get('/equipamento', tags=[equipamento_tag],
         responses={"200": EquipamentoViewSchema, "404": ErrorSchema})
def get_equipamento(query: EquipamentoBuscaSchema):    
    """Faz a busca por um equipamento cadastrado na base a partir do nome

    Args:
        nome (str): nome do equipamento
        
    Returns:
        dict: representação do equipamento e diagnóstico associado
    """
    
    equipamento_nome = query.name
    logger.debug(f"Coletando dados sobre produto #{equipamento_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    equipamento = session.query(Equipamento).filter(Equipamento.name == equipamento_nome).first()
    
    if not equipamento:
        # se o equipamento não foi encontrado
        error_msg = f"Equipamento {equipamento_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{equipamento_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Equipamento econtrado: '{equipamento.name}'")
        # retorna a representação do equipamento
        return apresenta_equipamento(equipamento), 200
   
    
# Rota de remoção de equipamento por nome
@app.delete('/equipamento', tags=[equipamento_tag],
            responses={"200": EquipamentoViewSchema, "404": ErrorSchema})
def delete_equipamento(query: EquipamentoBuscaSchema):
    """Remove um equipamento cadastrado na base a partir do nome

    Args:
        nome (str): nome do equipamento
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    equipamento_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre equipamento #{equipamento_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando equipamento
    equipamento = session.query(Equipamento).filter(Equipamento.name == equipamento_nome).first()
    
    if not equipamento:
        error_msg = "Equipamento não encontrado na base :/"
        logger.warning(f"Erro ao deletar equipamento '{equipamento_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(equipamento)
        session.commit()
        logger.debug(f"Deletado equipamento #{equipamento_nome}")
        return {"message": f"Equipamento {equipamento_nome} removido com sucesso!"}, 200