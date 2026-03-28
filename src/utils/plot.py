import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
from pathlib import Path

class plot:
    def __init__(self,diretorioGraficos='resultados/imagens'):
        self.diretorioGraficos=Path(diretorioGraficos)
        self.diretorioGraficos.mkdir(parents=True, exist_ok=True)
    def convergenciaAlgoritmo(self,historia,title="convergencia ABC",filename=None,show=True):
        plt.figure(figsize=(12,8))
        interacoes = range(len(historia['melhor performance'],label='melhor performance',linewidth=3,color='blue'))
        interacoes = range(len(historia['performance media'],label='performance media',linewidth=2.5,color='yellow',alpha=0.7))
        interacoes = range(len(historia['performance ruim'],label='performance ruim',linewidth=2.5,color='red',alpha=0.5))

        plt.xlabel('Iteracao', fontsize=14)
        plt.ylabel('performance', fontsize=14)
        plt.title(title, fontsize=16, fontweight='bold')
        plt.legend(loc='melhor')
        plt.grid(True, alpha=0.4)
        plt.yscale('log')  
        plt.tight_layout()
        

        
