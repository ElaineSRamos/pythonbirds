class Pessoa:
    def __init__(self, nome = None, idade = 35):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self): #sempre em um metodo deve-se declarar um atributo
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Luiza')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar()) # passagem implicita - quando vc chama o objeto pelo metodo nao é preciso passá-lo como primeiro parmetro
    print(p.nome)
    p.nome = 'Elaine'
    print( p.nome )
