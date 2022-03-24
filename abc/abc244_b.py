N = int(input())
T = input()

d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
v = 0
x, y = 0, 0
for i in range(N):
    if T[i] == 'S':
        dx, dy = d[v]
        x += dx
        y += dy
    else:
        v += 1
        v %= 4
print(x, y)
