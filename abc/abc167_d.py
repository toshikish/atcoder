N, K = map(int, input().split())
A = list(map(lambda s: int(s) - 1, input().split()))

V = [-1] * N
V[0] = 0
H = [0]
for i in range(1, K + 1):
    n = A[H[i - 1]]
    H.append(n)
    if V[n] != -1:
        start_L = V[n]
        L = H[start_L:i]
        break
    V[n] = i

if len(H) == K + 1:
    ans = H[K]
else:
    t = len(L)
    ans = L[(K - start_L) % t]
print(ans + 1)
