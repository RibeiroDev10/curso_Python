# 1º Exercício  
#entrada = input("Digite um número: ")

""" if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar is True:
        par_impar_texto = 'par'
    
    print(f'O número {entrada_int} é {par_impar_texto}')
    print()

else:
    print("Você não digitou um número inteiro.") """

""" try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar is True:
        par_impar_texto = 'par'
    
    print(f'O número {entrada_int} é {par_impar_texto}')
    print()
except:
    print("Você não digitou um número inteiro.") """




# 2º Exercício
""" entrada = input("Digite a hora em número inteiro: ")
try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print("Bom dia")
        print()
    elif hora >= 12 and hora <=17:
        print("Boa tarde")
        print()
    elif hora >= 18 and hora <= 23:
        print("Boa noite")
        print()
    else:
        print("Não conheço essa hora")
        print()
except:
    print("Por favor, digite apenas números inteiros.")
    print() """




# 3º Exercício
nome = input("Seu nome: ")
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4 :
        print("Seu nome é curto")
        print()
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print("Seu nome é normal")
        print()
    else:
        print("Seu nome é muito grande")
        print()
    print()
else:
    print("Digite mais de uma letra.")
    print()
