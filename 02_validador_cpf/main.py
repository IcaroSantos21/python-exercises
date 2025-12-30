from cpf_utils import *

while True:
    cpf = str(input('Entre com o cpf: '))
    
    cpf_digits = normalization_str(cpf)
    first_digit_validation(cpf_digits)
    second_digit_validation(cpf_digits)
    break