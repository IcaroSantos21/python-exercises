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

    return result

def second_digit_validation(digits):
    list_int = list(map(int, digits))
    total = 0
    for i in range(0, 10):
        
        num = 11 - i
        total += list_int[i] * num
    result = (total * 10) % 11

    return result