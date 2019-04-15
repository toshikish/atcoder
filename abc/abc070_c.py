from fractions import gcd
from functools import reduce

def lcm_base(x, y):
    return x * y // gcd(x, y)

def lcm(numbers):
    return reduce(lcm_base, numbers)

N = int(input())
T = [int(input()) for i in range(N)]
print(lcm(T))
