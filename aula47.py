palavra_secreta = 'perfume'
letras_acertadas = ''

while True:
    letra_digitada = input("Digite uma letra: ")

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
        if letra_secreta in letras_acertadas:
            print(letra_secreta)
