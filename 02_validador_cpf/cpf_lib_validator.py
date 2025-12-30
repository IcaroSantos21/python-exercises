from validate_docbr import CPF

def lib_validate_cpf(cpf):
    valid_cpf = CPF()
    validation = valid_cpf.validate(cpf)

    return validation