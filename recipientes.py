class Recipiente():
    def __init__(self):
        self._capacidade_volumetrica = None

    def define_capacidade_volumetrica(self, tamanho):
        self._capacidade_volumetrica = tamanho

class Copo(Recipiente):
    def tamanho_copo(self, tamanho):
        self.define_tamanho_copo()

    def define_tamanho_copo(self):
        raise NotImplementedError()
