import math

N = int(input())

x = math.ceil((math.sqrt(8 * N + 1) - 1) / 2)
S = x * (x + 1) // 2
ex = S - N
for i in range(1, x + 1):
    if i != ex:
        print(i)
