from cpf_utils import *

while True:
    cpf = input('Entre com o cpf: ')
    
    cpf_digits = normalization_str(cpf)
    print(cpf_digits)