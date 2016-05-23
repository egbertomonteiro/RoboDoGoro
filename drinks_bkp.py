from collections import defaultdict

class Drinks():
    def __init__(self):
        self._nome = None
        self._bebida = None
        self._qtdtotal = 0
        self.drink = {}

    def adiciona_qtd_e_bebida_ao_drink(self, nome, bebida, quantidade):
        _lista = [(nome, bebida, quantidade)]
        for nome, bebida, quantidade in _lista:
            self.drink.setdefault(nome,[]).append([bebida, quantidade])
        #print(list(self.drink.items()))

    def verifica_quantidade_total_drink(self):
        for nomedrink, listabebida in self.drink.items():
                self._qtdtotal = 0
                for beb, qtd in listabebida:
                    self._qtdtotal += qtd
                return 'Drink: {} QTD: {}'.format(nomedrink, self._qtdtotal)


class Amarula(Drinks):
    def __init__(self):
        self.quantidade = 30



if __name__ == '__main__':


    #Drink1 = Drinks()
    #print(Drink1.adiciona_qtd_e_bebida_ao_drink())
    #print(Drink1.drink)
    Drink2 = Drinks()
    Drink2.adiciona_qtd_e_bebida_ao_drink('Amarula','chocolate', 10)
    #print(Drink2.drink)
    Drink2.adiciona_qtd_e_bebida_ao_drink('Amarula', 'cafe', 40)
    Drink2.adiciona_qtd_e_bebida_ao_drink('Amarula', 'cafe', 1)
    Drink2.adiciona_qtd_e_bebida_ao_drink('Amarula', 'groselha', 5)
    print(Drink2.verifica_quantidade_total_drink())
    #print(Drink2.drink)

