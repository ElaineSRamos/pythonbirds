class Direcao:
    pass


"""
voce deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:
1- motor
2 - direção
o motor tera a responsabilidade de controlar a velocidade
ele oferece os seguintes atributos:
1) atributo de dado velocidade
2) metodo acelar que deverá incrementar a velocidade de uma unidade
3) metodo frear que deverá decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direação. Ela oferece os seguintes atributos:
1) valor de direação com valores possíveis: norte, sul, leste , oeste
2) metodo girar_a_direita
3) metoto_girar_a_esquerda


    Exemplo:
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'

    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    2
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'oeste'

"""

## declaração de uma constante

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


## fim declaração constante


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max( 0, self.velocidade )

    pass


class Direcao:
    rotacao_a_direita_dct = {NORTE: LESTE, LESTE:SUL, SUL: OESTE, OESTE:NORTE}
    rotacao_a_esquerda_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}
    def __init__(self):
        self.valor = NORTE

    pass

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor] #se fosse usar normalmente seria um if else
        return ()

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]  # se fosse usar normalmente seria um if else



class Carro():
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()
