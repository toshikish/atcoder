from math import sqrt

N, D = map(int, input().split())
X = [tuple(map(int, input().split())) for i in range(N)]

ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        sq_d = 0
        for k in range(D):
            sq_d += (X[i][k] - X[j][k]) ** 2
        d = sqrt(sq_d)
        if d - int(d) == 0:
            ans += 1
print(ans)
