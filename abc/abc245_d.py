N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

B = [0] * (M + 1)
for k in range(M, -1, -1):
    S = sum(A[N + k - i] * B[i]
            for i in range(M, k, -1) if 0 <= N + k - i <= N)
    B[k] = (C[N + k] - S) // A[N]

print(*B)
