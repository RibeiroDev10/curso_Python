import pprint as p

def nao_aceito_zero(d):
    if d ==0:
        # A palavra-chave raise em Python é usada para levantar (lançar) uma exceção. 
        # Uma exceção é uma sinalização de que algo excepcional e não esperado ocorreu durante a execução do programa. Quando você usa raise, 
        # está basicamente dizendo ao Python que algo deu errado e você está criando uma exceção para lidar com essa situação excepcional.
        raise ZeroDivisionError("Você está tentando dividir por zero!")
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    # Você está usando isinstance() para verificar se a variável n é do tipo float ou int. 
    # Se n não for uma instância de nenhum desses tipos (ou seja, se for de um tipo diferente), 
    # o código levanta uma exceção do tipo TypeError com uma mensagem de erro personalizada.
    if not isinstance(n, (float, int)):
        raise TypeError(
                f'{n} deve ser int ou float.',
                f'{tipo_n.__name__} enviado'
            )
    
    return True

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d

p(divide(8, 0))