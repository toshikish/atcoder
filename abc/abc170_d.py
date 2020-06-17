N = int(input())
A = list(map(int, input().split()))

A.sort()
C = [0] * A[-1]
for Ai in A:
    if C[Ai - 1] >= 1:
        C[Ai - 1] += 1
        continue
    i = Ai
    while i <= A[-1]:
        C[i - 1] += 1
        i += Ai
print(sum([C[Ai - 1] == 1 for Ai in A]))
