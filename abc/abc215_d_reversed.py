N, M = map(int, input().split())
A = list(map(int, input().split()))

exists = [False] * 100001
for Ai in A:
    exists[Ai] = True

F = set()
for i in range(2, M + 1):
    if any(exists[j] for j in range(i, 100001, i)):
        F.add(i)

K = [True] * (M + 1)
for i in F:
    for j in range(i, M + 1, i):
        K[j] = False

print(K.count(True) - 1)
for i in range(1, M + 1):
    if K[i]:
        print(i)
