print()

""" def duplicar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

def quadriplicar(numero):
    return numero * 4

print(duplicar(1))    
print(triplicar(1))    
print(quadriplicar(1)) """ 

def criar_multiplicador(multiplicador): 
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)

print(duplicar(2))

print()