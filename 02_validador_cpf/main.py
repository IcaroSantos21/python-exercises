from cpf_utils import *

while True:
    cpf = str(input('Entre com o cpf: '))
    if validate_cpf(cpf) == False:
        print('CPF Inválido')
        break
    print('CPF Válido')
    break