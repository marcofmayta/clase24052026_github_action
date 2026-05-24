import pytest
from app import sumar, dividir

def test_sumar():
    assert sumar(2, 3) == 5

def test_dividir():
    assert dividir(10, 2) == 5
    
def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)