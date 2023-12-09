from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = Temperatura do ar, Temperatura do Processo, Velocidade de rotação, Torque, Desgaste da Ferramenta, Saída

class Equipamento(Base):
    __tablename__ = 'equipamentos'
    
    id = Column(Integer, primary_key=True)
    name= Column("Name", String(50))
    temp= Column("TemperaturaDoAr[°C]", Integer)
    proc = Column("TemperaturaDoProcesso[°C]", Integer)
    vel = Column("VelocidadeDeRotacao[rpm]", Integer)
    tor = Column("Torque[Nm]", Float)
    des = Column("DesgasteDaFerramenta[min]", Integer)
    outcome = Column("Saida", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, temp:int, proc:int, vel:int, name:str,
                 tor:float, des:int, outcome:int, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Equipamento

        Arguments:
        name: nome do equipamento
            temp: temperatura do ar
            proc: temperatura do processo
            vel: velocidade de rotação
            tor: toque
            des: desgaste da ferramenta
            outcome: diagnóstico
            data_insercao: data de quando o equipamento foi inserido à base
        """
        self.name=name
        self.temp = temp
        self.proc = proc
        self.vel = vel
        self.tor = tor
        self.des = des
        self.outcome = outcome

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao