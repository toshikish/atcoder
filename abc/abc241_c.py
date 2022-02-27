N = int(input())
S = [input() for _ in range(N)]

ans = False

for i in range(N):
    for j in range(N - 5):
        if [S[i][j + k] for k in range(6)].count('#') >= 4:
            ans = True

for i in range(N - 5):
    for j in range(N):
        if [S[i + k][j] for k in range(6)].count('#') >= 4:
            ans = True

for i in range(N - 5):
    for j in range(N - 5):
        if [S[i + k][j + k] for k in range(6)].count('#') >= 4:
            ans = True
        if [S[i + k][j + 5 - k] for k in range(6)].count('#') >= 4:
            ans = True

print('Yes' if ans else 'No')
