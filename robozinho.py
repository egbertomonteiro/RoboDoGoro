class Robozinho():
    '''
    qtddeposicoes = Quantidade de posicoes/garrafas que o robo pode andar
    posicao = O robo sempre iniciará da posicao 0, ou posicao sem garrafa
    '''
    def __init__(self, qtdposicoes=6, posicao=0):
        self._posicoes = list(range(qtdposicoes))
        self._posicao = posicao

    def posicionar(self, posicao):
        #self.verificar_posicao_atual()
        #print(self._posicao)
        self.mover(posicao)

    def verificar_posicao_atual(self):
        #print('Movendo carrinho para {}'.format(self._posicao))
        return self._posicao

    def mover(self, posicao):
        self._posicao = posicao
        #mover o robo até no maximo a ultima posicao da lista qtddeposicoes

    def despejar_conteudo(self):
        self.posicionar(self._posicao)
        self.levanta_braco(self._tempo)

    def levanta_braco(self, tempo):
        self._tempo = tempo
        return 'Levantando braco por {} segundos ate o despejador'.format(tempo)

if __name__ == '__main__':
    robo = Robozinho()
    robo.posicionar(200)
    print(robo.verificar_posicao_atual())
    robo.posicionar(400)
    print(robo.levanta_braco(10))
    print(robo.verificar_posicao_atual())
