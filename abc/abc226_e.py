from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    Ui, Vi = map(lambda s: int(s) - 1, input().split())
    G[Ui].append((Vi, i))
    G[Vi].append((Ui, i))
MOD = 998244353

if N != M:
    ans = 0
else:
    ans = 1
    V = [False] * N
    E = [False] * M
    for i in range(N):
        if V[i]:
            continue
        V[i] = True
        v = 1
        e = 0
        q = deque(G[i])
        while q:
            j, k = q.popleft()
            if E[k]:
                continue
            E[k] = True
            e += 1
            if not V[j]:
                V[j] = True
                v += 1
            for l, m in G[j]:
                if E[m]:
                    continue
                q.append((l, m))
        if v == e:
            ans *= 2
            ans %= MOD
        else:
            ans = 0
            break
print(ans)
