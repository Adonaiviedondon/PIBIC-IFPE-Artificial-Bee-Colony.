import numpy as np

class analisador:

    def __init__(self, historico):
        self.historico = historico

    def melhoria(self):
        return np.min(self.historico)

    def final(self):
        return self.historico[-1]

    def Taxa_Convergencia(self):
        return np.mean(np.diff(self.historico))

    def summary(self):
        return {
            "melhorias": self.melhoria(),
            "final": self.final(),
            "convergencias": self.Taxa_Convergencia()
        }