class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome    
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Rafael', idade)
    

p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
print(p2.nome, p2.idade)
print(100 * '--')

# anonima
p3 = Pessoa.criar_sem_nome(10)
print(p3.nome)