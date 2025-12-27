from calculos import *
from menu import *

while True:
    exibir_menu()
    opcao = input("Digite aqui: ")
    if opcao == 's':
        print('saindo...')
        break
    selecao(opcao)