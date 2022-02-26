from collections import defaultdict

N, X = map(int, input().split())
d = defaultdict(int)
for _ in range(N):
    ai, bi = map(int, input().split())
    X -= ai
    d[bi - ai] += 1

ans = X >= 0
if ans:
    dp = set([0])
    for k, v in d.items():
        ndp = set()
        for i in range(v + 1):
            for dpi in dp:
                ndp.add(dpi + k * i)
        dp = ndp
    ans = X in dp
print('Yes' if ans else 'No')
