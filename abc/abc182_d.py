from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

B = list(accumulate(A))
M = [B[0]] * N + [0]
for i in range(1, N):
    M[i] = max(M[i - 1], B[i])
C = list(accumulate(B))
print(max([C[i] + M[i + 1] for i in range(N)] + [0]))
