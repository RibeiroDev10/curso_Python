import re # expressão regular

cpf_enviado_usuario = '113.120.066-76'.replace('.', '').replace('-', '').replace(' ', '')
cpf_enviado_usuario = re.sub(r'[^0-9]', '', '113.120.066-76')

entrada = input("CPF [746.824.890-70]")
entrada_e_sequencial = entrada[0]



nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado = 0
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11 
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print("CPF inválido")

print()
print('------------------------------------------')