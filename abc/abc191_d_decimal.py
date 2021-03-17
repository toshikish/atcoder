from decimal import Decimal
from math import ceil, floor

X, Y, R = map(Decimal, input().split())

ans = 0
for y in range(ceil(Y - R), floor(Y + R) + 1):
    sq = (R * R - (y - Y) * (y - Y)).sqrt()
    xl, xu = ceil(X - sq), floor(X + sq)
    ans += xu - xl + 1

print(ans)
