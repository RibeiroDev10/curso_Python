""" Calculadora com while """

while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite um operador (+-/*): ")

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)

        numeros_validos = True
    except Exception as error:
        numeros_validos = None

    if numeros_validos == None:
        print("Um ou ambos os numeros digitados são inválidos")
        continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print("Operador inválido.")
        continue

    if len(operador) > 1:
        print("Digite somente um operador.")
        continue

    print("Realizando sua conta, confira o resultado abaixo:")
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    else:
        print("Nunca deveria chegar aqui.")

    #################
    sair = input("Deseja sair? [s]im: ").lower().startswith('s')

    if sair is True:
        break