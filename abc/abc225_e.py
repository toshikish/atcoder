from functools import cmp_to_key


def compare(P0, P1):
    l = P1[0] * P0[1]
    r = P0[0] * P1[1]
    if l < r:
        return -1
    elif l > r:
        return 1
    else:
        return 0


N = int(input())
L = []
M = (1, -1)
for _ in range(N):
    xi, yi = map(int, input().split())
    if xi == 1:
        m = (xi, yi - 1)
        if compare(M, m) < 0:
            M = m
        continue
    L.append(((xi - 1, yi), (xi, yi - 1)))


def compareTuple(T0, T1):
    c1 = compare(T0[0], T1[0])
    if c1 != 0:
        return c1
    return compare(T0[1], T1[1])


L.sort(key=cmp_to_key(compareTuple))
ans = 0
c = (1, 0)
for e, b in L:
    if compare(b, c) < 0:
        continue
    ans += 1
    c = e
if M != (1, -1) and compare(M, c) >= 0:
    ans += 1
print(ans)
