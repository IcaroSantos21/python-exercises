def sum_(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def division(num1, num2):
    result = num1 / num2
    return result

def enhance(num1, num2):
    result = num1 ** num2
    return result

def percentage(num1, num2):
    result = num1 * (num2 / 100)
    return result

operators = {'+': sum_,
             '-': subtract,
             'x': multiply,
             '/': division,
             '*': enhance,
             '%': percentage,}