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

