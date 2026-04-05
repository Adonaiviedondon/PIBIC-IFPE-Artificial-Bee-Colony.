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

        interacoes = range(len(historia))
        
        plt.plot(interacoes, historia['best'], label='Melhor', linewidth=3,color='blue')
        plt.plot(interacoes, historia['best'], label='Melhor', linewidth=3,color='yellow',alpha=0.7)
        plt.plot(interacoes, historia['best'], label='Melhor', linewidth=3,color='red',alpha=0.5)
        

        plt.xlabel('Iteracao', fontsize=14)
        plt.ylabel('performance', fontsize=14)
        plt.title(title, fontsize=16, fontweight='bold')
        plt.legend(loc='best')
        plt.grid(True, alpha=0.4)
        plt.yscale('log')  
        plt.tight_layout()

        if filename:
            plt.savefig(self.diretorioGraficos / filename, dpi=400, bbox_inches='tight')
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
            plt.savefig(self.diretorioGraficos / filename, dpi=400, bbox_inches='tight')
        
        if show:
            plt.show()
        else:
            plt.close()

    def CriarTabelaEstatistica(self,estatistica,filename=None,show=True):

        if estatistica.empty:
            raise ValueError("dataframe sem dados estatisticos")
        

        tamanho_altura = max(2, len(estatistica) * 0.7)
        tamanho_largura = max(8, len(estatistica.columns) * 1.6)

        tamanho, areaTabela = plt.subplots(figsize=(tamanho_largura,tamanho_altura))

        areaTabela.axis('tight')
        areaTabela.axis('off')

        valores_formatados = estatistica.applymap(
            lambda i: f"{i:.3f}" if isinstance(i,float) else i).values
        
        tabela = areaTabela.table(
            cellText=valores_formatados,
            colLabels=estatistica.columns,
            rowLabels=estatistica.index,
            cellLoc='center',
            loc='center'
        )

        tabela.auto_set_font_size(False)
        tabela.set_fontsize(10)
        tabela.scale(1,1.6)   

        for (linha,coluna), celula in tabela.get_celld.items():
            if linha == 0:
                celula.set_facecolor('#4CAF54')
                celula.set_text_props(weight='bold',color='blue')
        
        plt.title('estatistica dos experimentos',fontsize =15,fontweight='bold',pad=22)
        
        if filename:
            plt.savefig(self.diretorioGraficos / filename, dpi=400, bbox_inches='tight')

        if show:
            plt.show()
        else:
            plt.close()


        
