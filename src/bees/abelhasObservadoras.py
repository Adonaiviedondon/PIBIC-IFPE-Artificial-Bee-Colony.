import numpy as np 
import random 

class abelhasObservadoras:
    def __init__(self,funçoesSolucao,valorEficiencia,contadorInteacoesSemMelhoria,eficiencia_fn):
        self.funçoesSolucao = funçoesSolucao
        self.valorEficiencia = valorEficiencia
        self.contadorInteacoesSemMelhoria = contadorInteacoesSemMelhoria
        self.eficiencia_fn = eficiencia_fn

    # def escolher_fontes():

    