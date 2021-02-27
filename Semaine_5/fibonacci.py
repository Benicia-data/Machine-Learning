def fibo(n):
    a, b = 0, 1
    if n == 0:
        return a
    for range _ in range(n):
        a,b = b, a + b
    return a    