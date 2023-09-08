nome_usuario = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Se os dados digitados forem diferentes de vazio, ou seja, preenchidos
if nome_usuario != '' and idade != '':
    print(f'Seu nome é {nome_usuario}')

    nome_invertido = nome_usuario[::-1]
    print(f'Seu nome invertido é: {nome_invertido}')

    if ' ' in nome_usuario:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome NÃO contém espaços')

    qtde_letras = len(nome_usuario)
    print(f'Seu nome contém: {qtde_letras} letras')

    primeira_letra = nome_usuario[0]
    print(f'A primeira letra do seu nome é {primeira_letra}')

    ultima_letra = nome_usuario[-1]
    print(f'A última letra do seu nome é {ultima_letra}')

    print(50 * '-')
    print()

elif nome_usuario == '' and idade == '':
    print("Desculpe, você deixou campos vazios")

    print(50 * '-')
    print()