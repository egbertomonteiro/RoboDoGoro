import logging

class Robozinho():
    '''
    qtddeposicoes = Quantidade de posicoes/garrafas que o robo pode andar
    posicao = O robo sempre iniciará da posicao 0, ou posicao sem garrafa
    '''
    def __init__(self, qtdposicoes=6, posicao=0):
        self._posicoes = list(range(qtdposicoes))
        self._posicao = posicao

    def posicionar(self, posicao):
        if posicao <= self._posicoes[-1]:
            self._posicao = posicao
            # mover o robo até no maximo a ultima posicao da lista qtddeposicoes
            self.mover(self._posicao)
        else:
            logging.error('Posicao {} fora do range. Maximo={}'.format(posicao, self._posicoes[-1]))

    def verificar_posicao_atual(self):
        #print('Movendo carrinho para {}'.format(self._posicao))
        return self._posicao

    def mover(self, posicao):
        ##<<<Chama o arduino>>>
        pass

    def despejar_conteudo(self):
        self.posicionar(self._posicao)
        self.levanta_braco(self._tempo)

    def levanta_braco(self, tempo):
        self._tempo = tempo
        #<<<Chama o arduino>>>
        return 'Levantando braco por {} segundos ate o despejador'.format(tempo)


if __name__ == '__main__':
    robo = Robozinho()
    robo.posicionar(1)
    print('Posicao Atual: ' + robo.verificar_posicao_atual().__str__())
    robo.posicionar(4)
    print('Posicao Atual: ' + robo.verificar_posicao_atual().__str__())
    print(robo.levanta_braco(10))
    robo.posicionar(7)
    print('Posicao Atual: ' + robo.verificar_posicao_atual().__str__())


