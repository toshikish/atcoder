N = int(input())
A = list(map(lambda s: int(s) - 1, input().split()))
B = list(map(lambda s: int(s) - 1, input().split()))
C = list(map(lambda s: int(s) - 1, input().split()))

nB = [0] * N
for Cj in C:
    nB[B[Cj]] += 1

print(sum(nB[Ai] for Ai in A))
