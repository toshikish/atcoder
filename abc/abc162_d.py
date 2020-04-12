N = int(input())
S = input()

L = ['R', 'G', 'B']
accum = [[0] * N for i in range(3)]
for i in range(3):
    l = L[i]
    if S[0] == l:
        accum[i][0] = 1
    for j in range(1, N):
        accum[i][j] = accum[i][j - 1] + (1 if S[j] == l else 0)

ans = 0
for j in range(1, N - 1):
    for i in range(j):
        if S[i] == S[j]:
            continue
        for k in range(3):
            if L[k] != S[i] and L[k] != S[j]:
                lk = L[k]
                ik = k
        ans += accum[ik][N - 1] - accum[ik][j]
        if 2 * (j + 1) - (i + 1) <= N and S[2 * (j + 1) - (i + 1) - 1] == lk:
            ans -= 1
print(ans)
