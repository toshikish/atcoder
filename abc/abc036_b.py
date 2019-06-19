N = int(input())
s = [list(input()) for i in range(N)]

a = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        a[j][N - i - 1] = s[i][j]

for i in range(N):
    print(''.join(a[i]))
