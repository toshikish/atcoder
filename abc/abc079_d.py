H, W = map(int, input().split())
c = [list(map(int, input().split())) for i in range(10)]
A = []
for i in range(H):
    A.extend(list(map(int, input().split())))

for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])

ans = 0
for Ai in A:
    if Ai != -1:
        ans += c[Ai][1]
print(ans)
