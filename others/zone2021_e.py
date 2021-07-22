from heapq import heappop, heappush

R, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
B = [list(map(int, input().split())) for _ in range(R - 1)]

INF = 1_000_000_007
d = [[[INF] * C for _ in range(R)] for _ in range(2)]
q = []


def update(x, f, r, c):
    if d[f][r][c] <= x:
        return
    d[f][r][c] = x
    heappush(q, (x, f, r, c))


update(0, 0, 0, 0)
while q:
    x, f, r, c = heappop(q)
    if d[f][r][c] != x:
        continue
    if f == 0:
        update(x + 1, 1, r, c)
        if c + 1 < C:
            update(x + A[r][c], 0, r, c + 1)
        if c - 1 >= 0:
            update(x + A[r][c - 1], 0, r, c - 1)
        if r + 1 < R:
            update(x + B[r][c], 0, r + 1, c)
    else:
        update(x, 0, r, c)
        if r - 1 >= 0:
            update(x + 1, 1, r - 1, c)

print(d[0][R - 1][C - 1])
