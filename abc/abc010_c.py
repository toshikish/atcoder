import math

txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())
P = []
for i in range(n):
    P.append(tuple(map(int, input().split())))

max_D = V * T
possible = False
for p in P:
    if math.sqrt((p[0] - txa) ** 2 + (p[1] - tya) ** 2) + math.sqrt((p[0] - txb) ** 2 + (p[1] - tyb) ** 2) <= max_D:
        possible = True
print('YES' if possible else 'NO')
