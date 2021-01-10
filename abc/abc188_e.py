from collections import defaultdict, deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
G = defaultdict(list)
I = defaultdict(list)
for i in range(M):
    Xi, Yi = map(lambda s: int(s) - 1, input().split())
    G[Xi].append(Yi)
    I[Yi].append(Xi)

ans = -1_000_000_000
Q = deque()
candid = defaultdict(int)
cnt = defaultdict(int)
len_G = [0] * N
len_I = [0] * N
for i in range(N):
    len_G[i] = len(G[i])
    len_I[i] = len(I[i])
for i in range(N):
    if len_G[i] == 0 and len_I[i] > 0:
        for nx in I[i]:
            candid[nx] = max(A[i], candid[nx])
            cnt[nx] += 1
            if cnt[nx] == len_G[nx]:
                Q.append(nx)
while len(Q) > 0:
    i = Q.popleft()
    mx = candid[i]
    ans = max(mx - A[i], ans)
    for nx in I[i]:
        candid[nx] = max(mx, A[i], candid[nx])
        cnt[nx] += 1
        if cnt[nx] == len_G[nx]:
            Q.append(nx)
print(ans)
