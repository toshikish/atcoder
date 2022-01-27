N = int(input())
A = list(map(int, input().split()))

C = [0] * N
for Ai in A:
    C[Ai - 1] += 1

print(C.index(3) + 1)
