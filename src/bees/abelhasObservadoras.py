import numpy as np 
import random 

class abelhasObservadoras:
    def __init__(self,EscolhasSolucao,valorEficiencia,contadorInteacoesSemMelhoria,eficiencia_fn):
        self.EscolhasSolucao = EscolhasSolucao
        self.valorEficiencia = valorEficiencia
        self.contadorInteacoesSemMelhoria = contadorInteacoesSemMelhoria
        self.eficiencia_fn = eficiencia_fn

    def escolher_fontes(self,probabilidades):
        np.random.choice(range(len(self.EscolhasSolucao)),probabilidades)
    def explore(self,index):
        tamanhoProblema = self.EscolhasSolucao.shape[1]
        proporcao = random.randint(0,tamanhoProblema - 1)






    