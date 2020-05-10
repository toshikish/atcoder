N, M, X = map(int, input().split())
C = [0] * N
A = []
for i in range(N):
    CA = list(map(int, input().split()))
    C[i] = CA[0]
    A.append(CA[1:])
INF = 1000000007

ans = INF
for i in range(1 << (N + 1)):
    S = [0] * M
    c = 0
    for j in range(N):
        if i >> j & 1 == 1:
            c += C[j]
            for k in range(M):
                S[k] += A[j][k]
    if all(Si >= X for Si in S):
        ans = min(c, ans)
print(ans if ans < INF else -1)
