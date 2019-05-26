from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(int)
for i in range(N):
    d[A[i]] += 1
for i in range(M):
    Bi, Ci = map(int, input().split())
    d[Ci] += Bi

res = N
ans = 0
for k, v in sorted(d.items(), reverse=True):
    ans += k * min(v, res)
    res -= v
    if res <= 0:
        break
print(ans)
