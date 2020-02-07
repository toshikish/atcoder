x, y, W = input().split()
x, y = int(x) - 1, int(y) - 1
c = [input() for i in range(9)]

V = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1),
     'RU': (1, -1), 'RD': (1, 1), 'LU': (-1, -1), 'LD': (-1, 1)}


def proceed(p, d):
    dx = d[0]
    if p[0] == 0 and d[0] < 0 or p[0] == 8 and d[0] > 0:
        dx *= -1
    dy = d[1]
    if p[1] == 0 and d[1] < 0 or p[1] == 8 and d[1] > 0:
        dy *= -1
    return ((p[0] + dx, p[1] + dy), (dx, dy))


ans = []
delta = V[W]
for i in range(4):
    ans.append(c[y][x])
    P = proceed((x, y), delta)
    x, y = P[0]
    delta = P[1]

print(''.join(ans))
