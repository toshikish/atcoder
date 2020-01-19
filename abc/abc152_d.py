N = int(input())


def msb(x):
    while x >= 10:
        x //= 10
    return x


n = [[0] * 9 for i in range(9)]

for i in range(1, N + 1):
    l = i % 10
    if l == 0:
        continue
    m = msb(i)
    n[l - 1][m - 1] += 1

ans = 0
for i in range(9):
    for j in range(9):
        ans += n[i][j] * n[j][i]
print(ans)
