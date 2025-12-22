import numpy as np;
from .AbelhasOperarias import AbelhaOperaria;
from .abelhasObservadoras import AbelhaObservadora;
from .AbelhasExploradoras import AbelhaExploradora;

class AbcControlador:
    def __init__(self,FunçoesParaSolução,num_operarias=60,num_observadoras=60,tamanhoProblema = 40,Num_Interacoes=110,Num_Falhas = 50):
        self.funçoesSoluçao = FunçoesParaSolução
        self.operarias = num_operarias
        self.observadoras = num_observadoras
        self.tamanhoProblema = tamanhoProblema
        self.interacoes = Num_Interacoes
        self.Num_Falhas = Num_Falhas

        self.opcaoSolucao = np.random.rand(num_operarias,tamanhoProblema)*110
        self.valorEficiencia = np.array([self.eficiencia_fn(fs) for fs in self.opcaoSolucao])
        self.contadorInteacoesSemMelhoria = np.zeros(AbelhaOperaria)

        self.operaria = AbelhaOperaria(self.opcaoSolucao,self.valorEficiencia,self.contadorInteacoesSemMelhoria,self.eficiencia_fn)
        self.observadora = AbelhaObservadora(self.opcaoSolucao,self.valorEficiencia,self.contadorInteacoesSemMelhoria,self.eficiencia_fn)
        self.exploradora = AbelhaExploradora(self.opcaoSolucao,self.valorEficiencia,self.contadorInteacoesSemMelhoria,self.eficiencia_fn,Num_Falhas)
def run(self):
    for interacao in range(self.interacoes):

        for i in range(self.operarias):
            self.operaria.explore(i)
        valor = 1.0 / (1.0 +  self.valorEficiencia)
        probabilidade = valor / np.sum(valor)
        for i in range(self.observadoras):
            index = self.observadora.selecionar_fonte(probabilidade)
            self.observadora.explore(index)
        for i in range(self.operarias):
            if self.contadorInteacoesSemMelhoria[i] > self.Num_Falhas:
                self.exploradora.atualiza(i)
        Melhor_Solucao = np.min(self.valorEficiencia)
        print(f"interacao {interacao} melhor opcao eh {Melhor_Solucao}")
        return self.opcaoSolucao[Melhor_Solucao],self.valorEficiencia[Melhor_Solucao]
            


