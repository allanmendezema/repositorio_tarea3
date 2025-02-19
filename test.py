# allan emanuel mendez mendez
#amendezm15@miumg.edu.gt
# calculator.py

class Calculator:
    def sum(self, a: float, b: float) -> float:
        return a + b
    
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

# test_calculator.py
import pytest
from calculator import Calculator

def test_sum_positive_numbers():

    calc = Calculator()
    

    result = calc.sum(3, 5)
    
    assert result == 8, "La suma de 3 + 5 debería ser 8"

def test_division_by_zero():

    calc = Calculator()
    
    
    with pytest.raises(ValueError) as exc_info:
        calc.divide(10, 0)
    
    assert str(exc_info.value) == "No se puede dividir por cero"