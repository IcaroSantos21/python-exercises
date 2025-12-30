# from cpf_utils import validate_cpf
from cpf_lib_validator import lib_validate_cpf

def test_cpf_valid():
    assert lib_validate_cpf("54711739025") is True
def test_cpf_format():
    assert lib_validate_cpf("547.117.390-25") is True
def test_cpf_invalid():
    assert lib_validate_cpf("111.111.111-11") is False
def test_cpf_has_only_digits():
    assert lib_validate_cpf("abc.def.ghi-jk") is False