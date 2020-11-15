from collections import defaultdict

N, W = map(int, input().split())
d = defaultdict(int)
for i in range(N):
    Si, Ti, Pi = map(int, input().split())
    d[Si] += Pi
    d[Ti] -= Pi

ans = True
S = 0
for t, p in sorted(d.items()):
    S += p
    if S > W:
        ans = False
        break
print('Yes' if ans else 'No')
