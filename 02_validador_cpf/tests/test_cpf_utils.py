from cpf_utils import validate_cpf

def test_cpf_valid():
    assert validate_cpf("54711739025") is True
def test_cpf_format():
    assert validate_cpf("547.117.390-25") is True
def test_cpf_invalid():
    assert validate_cpf("111.111.111-11") is False