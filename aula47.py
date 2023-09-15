import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True: 
    letra_digitada = input("Digite uma letra: ")
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    # letra secreta é o valor da percussão de cada índice da string (ex: string[i])
    ### resumo do for: para cada elemento (índice sequencial começando do 0 automáticamente)
    ### para cada elemento percorrido na string "palavra_secreta" faça...
    for letra_secreta in palavra_secreta:
        
        # se "p" for igual a "e"
        # se o indice do elemento da string, for igual a letra digitada faça...
        palavra_formada = ''
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

        print('Palavra formada: ', palavra_formada)

        if palavra_formada == palavra_secreta:
            os.system('clear')
            print("VOCÊ GANHOU!!! PARABÉNS")
            print('A palavra era: ', palavra_secreta)
            print('Tentativas: ', numero_tentativas)
            letras_acertadas = ''
            numero_tentativas = 0