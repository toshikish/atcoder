N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

def clip(F):
    u = 0
    while F[u] == '.' * N:
        u += 1
    d = N - 1
    while F[d] == '.' * N:
        d -= 1
    l = 0
    while all(F[i][l] == '.' for i in range(N)):
        l += 1
    r = N - 1
    while all(F[i][r] == '.' for i in range(N)):
        r -= 1
    return [F[i][l : r + 1] for i in range(u, d + 1)]

Sc = clip(S)
Hs, Ws = len(Sc), len(Sc[0])
Tc = clip(T)
Ht, Wt = len(Tc), len(Tc[0])
ans = False
if Hs == Ht and Ws == Wt:
    if all(Sc[i][j] == Tc[i][j] for i in range(Hs) for j in range(Ws)):
        ans = True
    if all(Sc[i][j] == Tc[Hs - i - 1][Ws - j - 1] for i in range(Hs) for j in range(Ws)):
        ans = True
if Hs == Wt and Ws == Ht:
    if all(Sc[i][j] == Tc[j][Wt - i - 1] for i in range(Hs) for j in range(Ws)):
        ans = True
    if all(Sc[i][j] == Tc[Ht - j - 1][i] for i in range(Hs) for j in range(Ws)):
        ans = True

print('Yes' if ans else 'No')
