N = int(input())
A = list(map(int, input().split()))

SQ = sum(Ai * Ai for Ai in A)
S = sum(A)
print(N * SQ - S * S)
