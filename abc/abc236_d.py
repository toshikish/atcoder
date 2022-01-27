N = int(input())
A = [list(map(int, input().split())) for _ in range(2 * N - 1)]

ans = 0
L = [False] * (2 * N)


def dfs(b):
    global L, ans
    if all(L):
        ans = max(b, ans)
        return
    i = L.index(False)
    L[i] = True
    for j in range(i + 1, 2 * N):
        if L[j]:
            continue
        L[j] = True
        dfs(b ^ A[i][j - i - 1])
        L[j] = False
    L[i] = False


dfs(0)
print(ans)
