from math import gcd

a = int(input())
b = int(input())
n = int(input())

lcm = a * b // gcd(a, b)
print(((n - 1) // lcm + 1) * lcm)
