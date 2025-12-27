from calculations import *
from menu import *

while True:
    display_menu()
    option = input("Digite aqui: ")
    valid_option = parse_option(option)
    if valid_option == 's':
        print('saindo...')
        break
    elif valid_option in operators:
        opertator = operators[valid_option]
        numbers = ask_number()
        print(opertator(*numbers))
    else:
       print('Erro: Opção selecionada inválida')