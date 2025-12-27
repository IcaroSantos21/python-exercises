from calculations import *
from menu import *
def ask_number():
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        return num1, num2

def validate_option():
    option = input("Digite aqui: ")
    valid_option = parse_option(option)
    return valid_option