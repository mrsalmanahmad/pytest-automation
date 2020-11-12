
import pytest

@pytest.mark.math
def test():
    a = 1
    b = 2
    c = 3
    assert a+b == c

@pytest.mark.math
def test1():
    a = 1 
    b = 2
    c = 3
    assert a+b == c

@pytest.mark.math
def test_devide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    assert 'division by zero' in str(e.value)


#         Parametrize test functions
product = [
    (2,3,6),
    (1,99,99),
    (0,99,0),
    (3,-2,-6),
    (-2,-2,4),
    (2,2,4)
]

@pytest.mark.math
@pytest.mark.parametrize('a,b,product',product)
def test_parameterize_func(a,b,product):
    assert a*b == product


