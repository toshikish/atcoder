import math

P = float(input())
x = max(1.5 * math.log2(P * math.log(2) / 1.5), 0)
print(x + P * math.pow(2, -x / 1.5))
