from math import isqrt


def ftoi(s):
    if '.' in s:
        i, j = s.split('.')
        return int(i) * 10000 + int(j.ljust(4, '0'))
    return int(s) * 10000


X, Y, R = map(ftoi, input().split())

ans = 0
for y in range(((Y - R) + 10000 - 1) // 10000, (Y + R) // 10000 + 1):
    y *= 10000
    sq = isqrt(R * R - (y - Y) * (y - Y))
    xl, xu = (X - sq + 10000 - 1) // 10000, (X + sq) // 10000
    ans += xu - xl + 1

print(ans)
