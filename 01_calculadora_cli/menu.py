def exibir_menu():
    print("----------CALCULADORA----------")
    print("           ESCOLHA:")
    print("           Soma = (+)")
    print("           Subtração = (-)")
    print("           Multiplicação = (x)")
    print("           Divisão = (/)")
    print("           Potenciação = (*)")
    print("           Porcentagem = (%)")
    print("           Sair = (s)")

def selecao(opcao):
    if opcao == '+':
        print("somando")
    elif opcao == '-':
        print("subtraindo")
    elif opcao == 'x':
        print("multiplicando")
    elif opcao == '/':
        print("dividindo")
    elif opcao == '*':
        print("potencializando")
    elif opcao == '%':
        print("porcentagem")
    else:
        print('Erro: Opção inválida')
