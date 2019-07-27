N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    s = min(A[i], B[i])
    A[i] -= s
    B[i] -= s
    ans += s
    s = min(A[i + 1], B[i])
    A[i + 1] -= s
    B[i] -= s
    ans += s

print(ans)
