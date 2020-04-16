from math import sqrt

N, P = map(int, input().split())

F = {}
for i in range(2, int(sqrt(P)) + 1):
    if P % i != 0:
        continue
    F[i] = 0
    while P % i == 0:
        P //= i
        F[i] += 1
if P > 1:
    F[P] = 1

ans = 1
for p in F.keys():
    ans *= p ** (F[p] // N)
print(ans)
