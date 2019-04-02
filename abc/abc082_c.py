from collections import defaultdict

N = int(input())
a = list(map(int, input().split()))

c = defaultdict(int)
for ai in a:
    c[ai] += 1

ans = 0
for k, v in c.items():
    if v > k:
        ans += v - k
    elif v < k:
        ans += v
print(ans)
