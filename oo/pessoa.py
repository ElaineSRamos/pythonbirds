class Pessoa:
    def cumprimentar(self): #sempre em um metodo deve-se declarar um atributo
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar()) # passagem implicita - quando vc chama o objeto pelo metodo nao é preciso passá-lo como primeiro parmetro
