import math, pytest
from app import operations as op

@pytest.mark.parametrize("a,b,res", [(2,3,5),(2,-3,-1),(0,0,0)])
def test_add(a,b,res): assert op.add(a,b)==res

def test_subtract(): assert op.subtract(10,4)==6
def test_multiply(): assert op.multiply(3,4)==12
def test_divide_ok(): assert op.divide(8,2)==4
def test_divide_zero(): 
    with pytest.raises(ZeroDivisionError): op.divide(1,0)

def test_power(): assert op.power(2,5)==32
def test_root_ok(): assert round(op.root(27,3),5)==3
def test_root_even_negative(): 
    with pytest.raises(ValueError): op.root(-8,2)

def test_modulus_ok(): assert op.modulus(10,3)==1
def test_modulus_zero():
    with pytest.raises(ZeroDivisionError): op.modulus(1,0)

def test_int_divide_ok(): assert op.int_divide(7,2)==3
def test_int_divide_zero():
    with pytest.raises(ZeroDivisionError): op.int_divide(1,0)

def test_percent_ok(): assert op.percent(25,100)==25.0
def test_percent_zero():
    with pytest.raises(ZeroDivisionError): op.percent(1,0)

def test_abs_diff(): assert op.abs_diff(10,3)==7
