from collections import defaultdict

N, K = map(int, input().split())
c = defaultdict(int)
for i in range(N):
    a, b = map(int, input().split())
    c[a] += b

counter = 0
for a, b in sorted(c.items(), key=lambda x: x[0]):
    counter += b
    if counter >= K:
        break
print(a)
