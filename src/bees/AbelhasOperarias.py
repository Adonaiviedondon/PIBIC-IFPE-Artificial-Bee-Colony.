import numpy as np 
import random

class AbelhasOperarias:
    def __init__(self,funçoesSolucao,valorEficiencia,contadorInteacoesSemMelhoria,eficiencia_fn):
        self.funçoesSolucao = funçoesSolucao
        self.valorEficiencia = valorEficiencia
        self.contadorInteacoesSemMelhoria = contadorInteacoesSemMelhoria
        self.eficiencia_fn = eficiencia_fn
    def explore(self, index: int):
        tamanhoProblema = self.opcaoSolucao.shape[1]

        dimensao = random.randint(0,tamanhoProblema - 1)

        mutante = np.copy(self.opcaoSolucao)
        mutante[dimensao] = mutante[dimensao] + (random.random() - 0.5) * 2

        eficiencia_Do_Mutante = self.eficiencia_fn(mutante)

        if eficiencia_Do_Mutante < self.valorEficiencia:
            self.funçoesSolucao[index]  = mutante
            self.valorEficiencia =[index] = mutante[dimensao]
            self.contadorInteacoesSemMelhoria[index] = 0
        else:
            self.contadorInteacoesSemMelhoria += 1