X, Y = map(int, input().split())

P = {3: 100000, 2: 200000, 1: 300000}
ans = 0
if X in P:
    ans += P[X]
if Y in P:
    ans += P[Y]
if X == Y == 1:
    ans += 400000
print(ans)
