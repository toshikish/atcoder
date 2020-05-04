from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())
L = []
for i in range(Q):
    ai, bi, ci, di = map(int, input().split())
    ai -= 1
    bi -= 1
    L.append((ai, bi, ci, di))

ans = 0
for A in combinations_with_replacement(range(M), N):
    r = 0
    for Li in L:
        if A[Li[1]] - A[Li[0]] == Li[2]:
            r += Li[3]
    ans = max(ans, r)

print(ans)
