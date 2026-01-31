import numpy as np

class AbelhasExploradoras:
    def __init__(self,EscolhasSolucao,valorEficiencia,contadorInteacoesSemMelhoria,eficiencia_fn,LimiteInteacoesSemMelhoria):
        self.EscolhasSolucao = EscolhasSolucao
        self.valorEficiencia = valorEficiencia
        self.contadorInteacoesSemMelhoria = contadorInteacoesSemMelhoria
        self.eficiencia_fn = eficiencia_fn
        self.LimiteInteacoesSemMelhoria = LimiteInteacoesSemMelhoria
    def atualiza(self , index):
       tamanhoProblema =  self.EscolhasSolucao.shape[1]

       SolucaoAtual = np.random.rand(tamanhoProblema) * 100
       self.EscolhasSolucao[index] = SolucaoAtual
       self.valorEficiencia[index] = self.eficiencia_fn(SolucaoAtual)
    #    contadorInteacoesSemMelhoria[index] = 0