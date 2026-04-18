import numpy as np;
from .AbelhasOperarias import AbelhaOperaria;
from .AbelhasObservadoras import AbelhaObservadora;
from .AbelhasExploradoras import AbelhaExploradora;

class AbcControlador:
    def __init__(self, eficiencia_fn,FunçoesParaSolução,num_operarias=45,num_observadoras=45,tamanhoProblema = 25,Num_Interacoes=100,Num_Falhas = 50,verbose=True):
        self.eficiencia_fn = eficiencia_fn 
        self.funçoesSoluçao = FunçoesParaSolução
        self.operarias = num_operarias
        self.observadoras = num_observadoras
        self.tamanhoProblema = tamanhoProblema
        self.interacoes = Num_Interacoes
        self.Num_Falhas = Num_Falhas
        self.verbose = verbose
        self.historico = {'best_fitness': [], 'mean_fitness': [], 'worst_fitness': []}

        self.opcaoSolucao = np.random.rand(num_operarias,tamanhoProblema)*100
        self.valorEficiencia = np.array([self.eficiencia_fn(fs) for fs in self.opcaoSolucao])
        self.contadorInteacoesSemMelhoria = np.zeros(num_operarias)

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
               index = self.observadora.escolher_fontes(probabilidade)
               self.observadora.explore(index)
           for i in range(self.operarias):
               if self.contadorInteacoesSemMelhoria[i] > self.Num_Falhas:
                   self.exploradora.atualiza(i)
           
           Melhor_Solucao = np.argmin(self.valorEficiencia)
           print(f"interacao {interacao} melhor opcao eh {Melhor_Solucao}")

        self.historico['best_fitness'].append(float(np.min(self.valorEficiencia)))
        self.historico['mean_fitness'].append(float(np.mean(self.valorEficiencia)))
        self.historico['worst_fitness'].append(float(np.max(self.valorEficiencia)))

        Melhor_Solucao = int(np.argmin(self.valorEficiencia))

        if self.verbose:
                print(f"Iteração {interacao + 1}/{self.interacoes} | "
                      f"Melhor fitness: {self.historico['best_fitness'][-1]:.6f} | "
                      f"Média: {self.historico['mean_fitness'][-1]:.6f}")
        return self.opcaoSolucao[Melhor_Solucao],self.valorEficiencia[Melhor_Solucao],self.historico
    
            


