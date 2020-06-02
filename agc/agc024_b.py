from collections import defaultdict

N = int(input())
P = [int(input()) for i in range(N)]

c = defaultdict(int)
for Pi in P:
    c[Pi] = c[Pi - 1] + 1

print(N - max(c.values()))
