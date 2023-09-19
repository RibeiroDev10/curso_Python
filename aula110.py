from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Rafael', 'nota': 'B'},
    {'nome': 'Pedro', 'nota': 'A'},
    {'nome': 'Carlos', 'nota': 'C'},
    {'nome': 'Leandro', 'nota': 'D'},
    {'nome': 'Manuel', 'nota': 'F'},
    {'nome': 'Tilia', 'nota': 'C'},
    {'nome': 'MauMau', 'nota': 'B'}
]


def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)


#for chave, grupo in grupos:
    #print(chave)
    #for aluno in grupo:
        #print(aluno)


#print()