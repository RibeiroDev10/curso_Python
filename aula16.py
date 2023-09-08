entrada = input('Você quer "entrar" ou "sair"? ')

# Validação do input
if entrada != "entrar" or entrada != "sair":
    print("Selecione um valor de input válido! (entrar ou sair)")
    print()
    valor_valido = input("Você deseja 'entrar' ou 'sair'? ")
    print()

# Autenticação conforme o valor do input
if valor_valido == "entrar":
    print("Você entrou no sistema!")
if valor_valido == "sair":
    print("Você saiu do sistema!")
    print()