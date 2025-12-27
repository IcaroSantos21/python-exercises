from calculations import *
from menu import *
from input_utils import *

def execute_operator(opcao):
    operator = operators[opcao]
    numbers = ask_number()
    return operator(*numbers)


while True:
    display_menu()
    valid_option = validate_option()
    if valid_option == 's':
        print('saindo...')
        break
    elif valid_option in operators:
        try:
            print(execute_operator(valid_option))
        except ZeroDivisionError as err:
            print(f'Erro: Tentativa de dividir por zero\nMensagem de erro: {err}')
        except ValueError as err:
            print(f'Erro: número digitado inválido\nMensagem de erro:{err}')
    else:
       print('Erro: Opção selecionada inválida')