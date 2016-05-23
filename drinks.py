from collections import defaultdict

class Drinks():
    def __init__(self, nome):
        self._nome = nome
        self._bebida = None
        self._qtdtotal = 0
        self.drink = {}

    def adiciona_qtd_e_bebida_ao_drink(self, bebida, quantidade):
        _lista = [(bebida, quantidade)]
        for bebida, quantidade in _lista:
            self.drink.setdefault(self._nome,[]).append([bebida, quantidade])
        #print(list(self.drink.items()))

    def verifica_quantidade_total_drink(self):
        for nomedrink, listabebida in self.drink.items():
                self._qtdtotal = 0
                for beb, qtd in listabebida:
                    self._qtdtotal += qtd
                return 'Drink: {} QTD: {}'.format(nomedrink, self._qtdtotal)

    def verifica_bebidas_do_drink(self):
        pass
        #raise NotImplementedError()


if __name__ == '__main__':

    drink2 = Drinks('Amarula')
    drink2.adiciona_qtd_e_bebida_ao_drink('chocolate', 10)
    drink2.adiciona_qtd_e_bebida_ao_drink('cafe', 40)
    drink2.adiciona_qtd_e_bebida_ao_drink('cafe', 1)
    drink2.adiciona_qtd_e_bebida_ao_drink('groselha', 5)
    print(drink2.verifica_quantidade_total_drink())
