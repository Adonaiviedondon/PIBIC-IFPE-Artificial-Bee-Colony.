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
        proporcao = random.randint(0,tamanhoProblema - 1)#dimensao eventual

        mutante = np.copy(self.EscolhasSolucao[index])
        mutante[proporcao] += (random.random() - 0.5) * 2#criação de uma solução mutante

        Eficiencia = self.eficiencia_fn(mutante)#avaliação

        if Eficiencia < self.valorEficiencia[index]:
            self.EscolhasSolucao[index] = mutante
            self.valorEficiencia[index] = Eficiencia
            self.contadorInteacoesSemMelhoria = 0
        else:
            self.contadorInteacoesSemMelhoria +=1








    