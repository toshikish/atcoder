H, W, D = map(int, input().split())
A = [list(map(lambda s: int(s) - 1, input().split())) for i in range(H)]
Q = int(input())
queries = [tuple(map(lambda s: int(s) - 1, input().split())) for i in range(Q)]

T = {}
for i in range(H):
    for j in range(W):
        T[A[i][j]] = (i, j)
accum = [[0] for i in range(D)]
for i in range(D):
    for j in range(i + D, H * W, D):
        p = T[j - D]
        n = T[j]
        accum[i].append(accum[i][-1] + abs(p[0] - n[0]) + abs(p[1] - n[1]))

for query in queries:
    r = query[0] % D
    print(accum[r][query[1] // D] - accum[r][query[0] // D])
