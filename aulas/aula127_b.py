import json
from aula127_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    
    print(p1)
    print(100 * '-')