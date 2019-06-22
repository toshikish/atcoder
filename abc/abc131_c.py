import math

A, B, C, D = map(int, input().split())
lcm = C * D // math.gcd(C, D)

def f(n):
    return n - (n // C + n // D - n // lcm)

print(f(B) - f(A - 1))
