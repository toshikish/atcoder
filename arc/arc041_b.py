N, M = map(int, input().split())
b = [list(map(int, list(input()))) for i in range(N)]

a = [[0] * M for i in range(N)]
for i in range(1, N - 1):
    for j in range(1, M - 1):
        a[i][j] = b[i - 1][j]
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            b[i + di][j + dj] -= a[i][j]

for i in range(N):
    print(''.join(list(map(str, a[i]))))
