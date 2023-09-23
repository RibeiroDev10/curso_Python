import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('Rafael', 20)
p3 = Pessoa('Luiz', 40)

# criando a lista iterável, vamos usar o vars() para pegar os atributos da classe como um dict.
# podemos usar também o dander __dict__
bd = [vars(p1), p2.__dict__, vars(p3)]

# adiando a execução do json.dump com uma função
def fazer_dump():
    # usando o JSON
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        # jogando os dados (bd) dentro do arquivo (aula127.json, que será criado dinamicamente)
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()