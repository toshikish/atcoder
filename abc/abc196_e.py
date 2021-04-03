N = int(input())
INF = 10 ** 15
h = INF
l = -INF
m = 0
for _ in range(N):
    ai, ti = map(int, input().split())
    if ti == 1:
        h += ai
        l += ai
        m += ai
    elif ti == 2:
        h = max(h, ai)
        l = max(l, ai)
    else:
        h = min(h, ai)
        l = min(l, ai)

Q = int(input())
x = list(map(int, input().split()))
for xi in x:
    print(min(h, max(l, xi + m)))
