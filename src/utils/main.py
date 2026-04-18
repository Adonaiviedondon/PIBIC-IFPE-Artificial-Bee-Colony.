import sys
import numpy as np
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from ABC.controlador import ABCController
from ABC.FuncoesParaSolucao import (
    Esfera,
    Rastringin,
    BananaRosenBrock,
    DimensaoVetorAckley,
    OtimizacaoGlobalGriewank,
    OtimizaçaoZakharov
)
from utils.analisador import ResultadoAnalisador
from utils.plot import plot
from utils.ajudantes import (
    DataDadosArquivos,
    LoggingExperimentos,
    BarraProgresso,
    printHeader,
    printSecao,
)

def testeSimples():
    printHeader("ABC — Teste Simples (Esfera)")

    abc = ABCController(
        fitness_function = Esfera,
        num_operarias    = 45,
        num_observadoras = 45,
        problem_size     = 10,
        max_iterations   = 50,
        limit            = 20,
        bounds           = (-100, 100),
        verbose          = True
    )

    melhor_solucao, melhor_fitness, historico = abc.run()

    print(f"\nMelhor fitness encontrado: {melhor_fitness:.6f}")
    plot(historico, nome_funcao='Esfera', pasta='data/results')


def rodarExperimentos():
    FUNCOES = {
        'Esfera':        Esfera,
        'Rastrigin':     Rastringin,
        'Rosenbrock':    BananaRosenBrock,
        'Ackley':        DimensaoVetorAckley,
        'Griewank':      OtimizacaoGlobalGriewank,
        'Zakharov':      OtimizaçaoZakharov,
    }

    NUM_EXECUCOES    = 32
    NUM_ITERACOES    = 110
    TAMANHO_PROBLEMA = 12
    NUM_FALHAS       = 40

    logger   = LoggingExperimentos('data/results')
    arquivos = DataDadosArquivos('data/results')

    for nome, fn in FUNCOES.items():
        printSecao(f"Função: {nome}")

        melhores   = []
        historicos = []
        barra      = BarraProgresso(NUM_EXECUCOES, nome)

        for execucao in range(NUM_EXECUCOES):
            abc = ABCController(
                fitness_function = fn,
                num_operarias    = 45,
                num_observadoras = 45,
                problem_size     = TAMANHO_PROBLEMA,
                max_iterations   = NUM_ITERACOES,
                limit            = NUM_FALHAS,
                bounds           = (-100, 100),
                verbose          = False
            )

            melhor_solucao, melhor_fitness, historico = abc.run()
            melhores.append(melhor_fitness)
            historicos.append(historico)
            barra.atualizar(execucao + 1)
            logger.registrar(nome, execucao + 1, melhor_fitness)

        
        analisador = ResultadoAnalisador(nome, melhores, historicos)
        analisador.salvar('data/results')
        plot(historicos, nome_funcao=nome, pasta='data/results')

        printSecao(f"Resultados — {nome}")
        analisador.imprimir_resumo()


if __name__ == '__main__':
    
    testeSimples()