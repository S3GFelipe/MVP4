from pydantic import BaseModel
from typing import Optional, List
from model.equipamento import Equipamento
import json
import numpy as np

class EquipamentoSchema(BaseModel):
    """ Define como um novo equipamento a ser inserido deve ser representado
    """
    name: str = "Motor Bomba"
    temp: int = 20
    proc: int = 30
    vel: int = 50
    tor: int = 1500
    des: int = 15
    
    
class EquipamentoViewSchema(BaseModel):
    """Define como um equipamento será retornado
    """
    id: int = 1
    name: str = "Motor Bomba"
    temp: int = 20
    proc: int = 30
    vel: int = 50
    tor: int = 1500
    des: int = 15
    outcome: int = None
    
class EquipamentoBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do equipamento.
    """
    name: str = "Motor Bomba"

class ListaEquipamentosSchema(BaseModel):
    """Define como uma lista de equipamentos será representada
    """
    equipamentos: List[EquipamentoSchema]

    
class EquipamentoDelSchema(BaseModel):
    """Define como um equipamento para deleção será representado
    """
    name: str = "Motor Bomba"
    
# Apresenta apenas os dados de um equipamento    
def apresenta_equipamento(equipamento: Equipamento):
    """ Retorna uma representação do equipamento seguindo o schema definido em
        EquipamentoViewSchema.
    """
    return {
        "id": equipamento.id,
        "name": equipamento.name,
        "temp": equipamento.temp,
        "proc": equipamento.proc,
        "vel": equipamento.vel,
        "tor": equipamento.tor,
        "des": equipamento.des,
        "outcome": equipamento.outcome
    }
    
# Apresenta uma lista de equipamentos
def apresenta_equipamentos(equipamentos: List[Equipamento]):
    """ Retorna uma representação do equipamento seguindo o schema definido em
        EquipamentoViewSchema.
    """
    result = []
    for equipamento in equipamentos:
        result.append({
            "id": equipamento.id,
            "name": equipamento.name,
            "temp": equipamento.temp,
            "proc": equipamento.proc,
            "vel": equipamento.vel,    
            "tor": equipamento.tor,
            "des": equipamento.des,
            "outcome": equipamento.outcome
        })

    return {"equipamentos": result}

