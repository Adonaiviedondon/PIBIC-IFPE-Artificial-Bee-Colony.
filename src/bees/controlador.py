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

        self_opcaoSolucao = np.random.rand(num_operarias,tamanhoProblema)*110
        self_valorEficiencia = np.array([self.eficiencia_fn(fs) for fs in self_opcaoSolucao])
        self.contadorInteacoesSemMelhoria = np.zeros(AbelhaOperaria)

        self.operaria = AbelhaOperaria(self_opcaoSolucao,self_valorEficiencia,self.contadorInteacoesSemMelhoria,self.eficiencia_fn)
        self.observadora = AbelhaObservadora(self_opcaoSolucao,self_valorEficiencia,self.contadorInteacoesSemMelhoria,self.eficiencia_fn)
        self.exploradora = AbelhaExploradora(self_opcaoSolucao,self_valorEficiencia,self.contadorInteacoesSemMelhoria,self.eficiencia_fn)
def run(self):
    for interacao in range(self.interacoes):
        

        


        

