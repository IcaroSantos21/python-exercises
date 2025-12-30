from cpf_utils import *
from cpf_lib_validator import *
from menu import *

while True:
    display_menu()
    option = input('Digite aqui:')
    valid_option = parse_option(option)
    if valid_option == 'v':
        cpf = str(input('Entre com o cpf: '))
        # if validate_cpf(cpf) == False
        if lib_validate_cpf(cpf) == False:
            print('CPF Inválido')
        print('CPF Válido')
    elif valid_option == 's':
        print('saindo...')
        break
    else:
        print('Opção inválida')