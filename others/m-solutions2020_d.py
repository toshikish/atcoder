N = int(input())
A = list(map(int, input().split()))

P = []
m = A[0]
for i in range(1, N):
    if A[i] < A[i - 1]:
        if m != A[i - 1]:
            P.append((m, A[i - 1]))
        m = A[i]
if m < A[N - 1]:
    P.append((m, A[N - 1]))

ans = 1000
for p in P:
    ans += (p[1] - p[0]) * (ans // p[0])
print(ans)
