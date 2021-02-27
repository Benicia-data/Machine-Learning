from fibonacci import fibo
from random import randint

def test_fibo_elementaire():
    assert fibo(0) == 0
    assert fibo(1) == 1
    
def test_fibo():
    for n in range(2, 10):
        assert fibo(n) == fibo(n - 1) + fibo(n - 2)
        
def test_fibo_alea():
    n = randint(2, 50)
    assert fibo(n) == fibo(n - 1) + fibo(n - 2)