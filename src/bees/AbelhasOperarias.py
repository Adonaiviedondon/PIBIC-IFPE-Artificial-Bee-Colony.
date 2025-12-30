import numpy as np 
import random

class AbelhasOperarias:
    def __init__(self,eficiencia_fn,opcaoSolucao,contadorInteacoesSemMelhoria,valorEficiencia):
        self.eficiencia_fn = eficiencia_fn
        self.opcaoSolucao = opcaoSolucao
        self.contadorInteacoesSemMelhoria = contadorInteacoesSemMelhoria
        self.valorEficiencia = valorEficiencia
    def explore(self, index: int):
        tamanhoProblema = self.opcaoSolucao.shape[1]

        dimensao = random.randint(0,tamanhoProblema - 1)

        mutante = np.copy(self.opcaoSolucao)