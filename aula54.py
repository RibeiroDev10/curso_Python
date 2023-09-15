import os

lista = []
while True:
    print("Selecione uma opção:")
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        # pega o valor/dado que usuario digitou e adiciona na lista
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            # passando o indice que o usuario digitou para inteiro
            indice = int(indice_str)
            # delete o indice (que foi transformado em int) da lista
            del lista[indice]
        except:
            print("Não foi possível apagar este índice")
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print("Nada para listar")

        for indice, valor in enumerate(lista):
            print(indice, valor)
    else:
        print("Por favor, escolha: I, A ou L")