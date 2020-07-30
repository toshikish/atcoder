N = int(input())
S = [list(input()) for i in range(N)]

ans = 0
for i in range(N):
    for j in range(N - 1, -1, -1):
        if S[i][j] == 'o':
            continue
        ans += 1
        S[i][:j] = ['o'] * j
        if i + 1 < N:
            S[i + 1][j:] = ['o'] * (N - j)
        break
    else:
        continue
print(ans)
