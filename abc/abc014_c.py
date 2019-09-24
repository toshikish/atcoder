from collections import defaultdict

n = int(input())

c = defaultdict(int)
for i in range(n):
    a, b = map(int, input().split())
    c[a] += 1
    c[b + 1] -= 1

popularity = 0
ans = 0
for k, v in sorted(c.items()):
    popularity += v
    ans = max(ans, popularity)
print(ans)
