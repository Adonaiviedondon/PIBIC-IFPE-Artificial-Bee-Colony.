import numpy as np;
from .AbelhasOperarias import AbelhaOperaria;
from .abelhasObservadoras import AbelhaObservadora;
from .AbelhasExploradoras import AbelhaExploradora;

class AbcControlador:
    def __init__(self,FunçoesParaSolução,num_operarias=60,num_observadoras=60,tamanhoProblema = 40,Num_Interações=110,Num_Falhas = 50):
        self.funçoesSoluçao = FunçoesParaSolução,
        self.operarias = num_operarias,
        self.observadoras = num_observadoras,
        self.tamanhoProblema = tamanhoProblema,
        self.interações = Num_Interações,
        

