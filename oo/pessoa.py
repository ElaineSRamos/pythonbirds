class Pessoa:
    def __init__(self, *filhos, nome = None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos) #objetos complexos podem ser passados como parametro tb

    def cumprimentar(self): #sempre em um metodo deve-se declarar um atributo
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome ='Renzo')
    luciano = Pessoa(renzo, nome = 'Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar()) # passagem implicita - quando vc chama o objeto pelo metodo nao é preciso passá-lo como primeiro parmetro
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)

    luciano.sobrenome = 'Ramalho' #criando um atributo dinamicamente. Nenhum outro
    #objeto que utilize esta classe será afetada, caso este seja usado.
    del luciano.filhos #deletando o atributo dinamicamente - nao é uma boa pratica]

    print(luciano.__dict__) #visualizacao da forma  u sera utilizada paar
    print(renzo.__dict__)
#    p.nome = 'Elaine'
#    print( p.nome )
