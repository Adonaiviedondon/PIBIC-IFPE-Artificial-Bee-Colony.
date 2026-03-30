import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
from pathlib import Path

class plot:
    def __init__(self,diretorioGraficos='resultados/imagens'):
        self.diretorioGraficos=Path(diretorioGraficos)
        self.diretorioGraficos.mkdir(parents=True, exist_ok=True)
    def PlotConvergenciaAlgoritmo(self,historia,title="convergencia ABC",filename=None,show=True):
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

        if filename:
            plt.savefig(self.save_dir / filename, dpi=400, bbox_inches='tight')
        if show:
            plt.show()
        else:
            plt.close()
    def PlotConvergenciaMultipla(self,historicos,title='comparativo das convergencias',filename=None,show=True):
        plt.figure(15,12)
        colors = plt.cm.tab10(np.linspace(0, 1, len(historicos)))

        for i, (name, history) in enumerate(historicos.items()):
            iterations = range(len(history['melhor performance']))
            plt.plot(iterations, history['melhor performance'], 
                    label=name, linewidth=4, color=colors[i])
        
        plt.xlabel('Iteração', fontsize=14)
        plt.ylabel('Melhor Fitness', fontsize=14)
        plt.title(title, fontsize=16, fontweight='bold')
        plt.legend(loc='best')
        plt.grid(True, alpha=0.3)
        plt.yscale('log')
        plt.tight_layout()

        if filename:
            plt.savefig(self.save_dir / filename, dpi=400, bbox_inches='tight')
        
        if show:
            plt.show()
        else:
            plt.close()
        

        
