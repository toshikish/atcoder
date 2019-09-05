from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

c = defaultdict(int)
c[0] = 1
s = 0
for i in range(N):
    s += A[i]
    c[s] += 1

ans = 0
for n in c.values():
    ans += n * (n - 1) // 2
print(ans)
