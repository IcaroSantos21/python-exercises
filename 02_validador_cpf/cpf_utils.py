def normalization_str(string):
    str_normalization = string.strip().replace('-', '').replace('.', '')
    return str_normalization

def first_digit_validation(digits):
    list_int = list(map(int, digits))
    total = 0
    for i in range(0, 9):
        
        num = 10 - i
        total += list_int[i] * num
    result = (total * 10) % 11
    if result == 10:
        return 0
    return result

def second_digit_validation(digits):
    list_int = list(map(int, digits))
    total = 0
    for i in range(0, 10):
        
        num = 11 - i
        total += list_int[i] * num
    result = (total * 10) % 11
    if result == 10:
        return 0

    return result

def validate_cpf(cpf: str) -> bool:
    cpf_str = normalization_str(cpf)  
    if len(cpf_str) != 11:
        return False
    if len(set(cpf_str)) == 1:
        return False
    
    first_digit = str(first_digit_validation(cpf_str))
    if first_digit != cpf_str[9]:
        return False
    
    second_digit = str(second_digit_validation(cpf_str))
    if second_digit != cpf_str[10]:
        return False
    return True