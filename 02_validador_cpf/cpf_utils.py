# retorna somente os digitos do cpf
def sanitize_cpf(cpf: str) -> str:
    cpf_sanitize = cpf.strip().replace('-', '').replace('.', '')
    return cpf_sanitize

# verifica se é apenas digitos
def has_only_digits(cpf):
    if cpf.isdigit() is False:
        return False
    return True

# Verifica quantos digitos possui
def length_cpf(cpf):
    if len(cpf) != 11:
        return False
    return True
    
# Verifica se o cpf é uma sequência de números
def is_repeated_sequence(cpf):
    if len(set(cpf)) == 1:
        return True
    return False

# válida o primeiro dígito verificador
def digit_validation(digits, final, load):
    list_int = list(map(int, digits))
    total = 0
    for i in range(0, final):
        
        num = load - i
        total += list_int[i] * num
    result = (total * 10) % 11
    if result == 10:
        return 0
    return result


# retorna se o cpf é valido ou não
def validate_cpf(cpf: str) -> bool:
    cpf_str = sanitize_cpf(cpf)
    
    if not has_only_digits(cpf_str):
        return False
    
    if not length_cpf(cpf_str):
        return False
      
    if is_repeated_sequence(cpf_str):
        return False
    
    first_digit = str(digit_validation(cpf_str, 9, 10))
    if first_digit != cpf_str[9]:
        return False
    
    second_digit = str(digit_validation(cpf_str, 10, 11))
    if second_digit != cpf_str[10]:
        return False
    return True