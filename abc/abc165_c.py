N, M, Q = map(int, input().split())
L = []
for i in range(Q):
    ai, bi, ci, di = map(int, input().split())
    ai -= 1
    bi -= 1
    L.append((ai, bi, ci, di))


def dfs(A):
    if len(A) == N:
        r = 0
        for Li in L:
            if A[Li[1]] - A[Li[0]] == Li[2]:
                r += Li[3]
        return r
    r = 0
    for i in range(A[-1], M + 1):
        r = max(r, dfs(A + [i]))
    return r


print(dfs([1]))
