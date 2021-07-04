N, K = map(int, input().split())
a = list(map(int, input().split()))

ans = [K // N] * N
A = sorted([(a[i], i) for i in range(N)])
for i in range(K % N):
    ans[A[i][1]] += 1

for i in range(N):
    print(ans[i])
