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
    abc = ABCController(
        fitness_function=Esfera,
        num_operarias=45,
        num_observadoras=45,
        problem_size=10,
        max_iterations=50,
        limit=20,
        bounds=(-100, 100),
        verbose=True
    )
    

