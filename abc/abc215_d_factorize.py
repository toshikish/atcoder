N, M = map(int, input().split())
A = list(map(int, input().split()))

F = set()
for Ai in set(A):
    if Ai == 1:
        continue
    i = 2
    while i * i <= Ai:
        while Ai % i == 0:
            F.add(i)
            Ai //= i
        i += 1 if i == 2 else 2
    if Ai != 1:
        F.add(Ai)

K = [True] * (M + 1)
for i in F:
    if i > M or not K[i]:
        continue
    for j in range(i, M + 1, i):
        K[j] = False

print(K.count(True) - 1)
for i in range(1, M + 1):
    if K[i]:
        print(i)
