import json
import numpy as np
from datetime import datetime
from pathlib import Path


class DataDadosArquivos:
    def salvarJson(data,filepath):
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True,  exist_ok =True)
        data= DataDadosArquivos._conversor_numpy(data)
        with open(filepath, 'w+',encoding='utf-8') as f:
            json.dump(data, f ,indent=2,ensure_ascii=False)
        print(f"salvando dados em {filepath}")
    
    def _conversor_numpy(objeto):
        if isinstance(objeto, np.ndarray):
            return objeto.tolist()
        elif isinstance(objeto, np.integer):
            return int(objeto)
        elif isinstance(objeto, np.floating):
            return float(objeto)
        elif isinstance(objeto, dict):
            return {k: DataDadosArquivos._conversor_numpy(v) for k, v in objeto.items()}
        elif isinstance(objeto, list):
            return [DataDadosArquivos._conversor_numpy(i) for i in objeto]
        return objeto

class LoggingExperimentos:
    def __init__(self, verbose=True):
        self.verbose = verbose

    def info(self, msg):
        print(f"[INFO] {msg}")

    def Aviso(self, msg):
        print(f"[AVISO!!] {msg}")

    def error(self, msg):
        print(f"[ERRO] {msg}")

    def sucesso(self, msg):
        print(f"[OK] {msg}")
class BarraProgresso:
    def __init__(self, total, descricao='Progresso'):
        self.total = total
        self.atual = 0
        self.descricao = descricao

    def atualizar(self):
        self.atual += 1
        porcentagem = (self.atual / self.total) * 100
        preenchido = int(40 * self.atual / self.total)
        barra = '█' * preenchido + '|' * (40 - preenchido)
        print(f"\r{self.descricao}: |{barra}| {porcentagem:.2f}%",
              end='', flush=True)
        if self.atual >= self.total:
            print()
def printHeader(texto, largura=70):
    print(f"\n{'=' * largura}")
    print(f"{texto.center(largura)}")
    print(f"{'=' * largura}\n")


def printSecao(texto, largura=70):
    print(f"\n{'-' * largura}")
    print(f"  {texto}")
    print(f"{'-' * largura}")