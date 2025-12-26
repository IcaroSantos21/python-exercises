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

while True:
    exibir_menu()
    opcao = input("Digite aqui: ")

    if opcao == 's':
        print("saindo...")
        break
    elif opcao == '+':
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
        print('ERRO: opção inválida')