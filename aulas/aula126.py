class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade, prof):
        self.nome = nome
        self.idade = idade
        self.profissao = prof
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
dados = {'nome': 'Rafael', 'idade': 20, 'prof':'Programador'}
p1 = Pessoa(**dados)
# p1 = Pessoa(nome='Rafael', idade=20, prof='Programador')

print(vars(p1))
print(p1.__dict__)
print(vars(p1))