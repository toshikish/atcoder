L, X, Y, S, D = map(int, input().split())

d = D - S if D >= S else L - (S - D)
r = L - d
ans = d / (X + Y)
if X < Y:
    ans = min(ans, r / (Y - X))
print(ans)
