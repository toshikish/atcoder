N, M = map(int, input().split())
P = [tuple(map(int, input().split())) for i in range(M)]

A = [-1] * N
ans = 0
for si, ci in P:
    si -= 1
    if si == ci == 0 and N >= 2:
        ans = -1
        break
    if A[si] == -1:
        A[si] = ci
    elif A[si] != ci:
        ans = -1
        break
if ans == 0:
    if A[0] == -1:
        A[0] = 0 if N == 1 else 1
    for i in range(1, N):
        if A[i] == -1:
            A[i] = 0
    ans = ''.join(list(map(str, A)))
print(ans)
