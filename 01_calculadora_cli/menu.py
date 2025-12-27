def display_menu():
    print("----------CALCULADORA----------")
    print("           ESCOLHA:")
    print("           Soma = (+)")
    print("           Subtração = (-)")
    print("           Multiplicação = (x)")
    print("           Divisão = (/)")
    print("           Potenciação = (*)")
    print("           Porcentagem = (%)")
    print("           Sair = (s)")

def parse_option(option):
    return option.lower().strip()

def ask_number():
        num1 = input('Digite o primeiro número: ')
        num2 = input('Digite o segundo número: ')
        return(num1 + num2)