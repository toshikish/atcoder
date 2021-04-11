from math import isqrt

R, X, Y = map(int, input().split())

dsq = X * X + Y * Y
Rsq = R * R
nsq = dsq // Rsq
n = isqrt(nsq)
while dsq > n * n * Rsq:
    n += 1

print(2 if dsq < Rsq else n)
