from calculations import *
from menu import *

while True:
    display_menu()
    option = input("Digite aqui: ")
    valid_option = parse_option(option)
    if valid_option == 's':
        print('saindo...')
    elif valid_option in operators:
        print('existe o operador')
    else:
       print('Erro: Opção selecionada inválida')