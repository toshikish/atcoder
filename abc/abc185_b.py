N, M, T = map(int, input().split())
Q = [tuple(map(int, input().split())) for i in range(M)]

ans = True
r = N
bi = 0
for Ai, Bi in Q:
    r -= Ai - bi
    if r <= 0:
        ans = False
        break
    r += Bi - Ai
    r = min(r, N)
    bi = Bi
r -= T - bi
ans &= r > 0
print('Yes' if ans else 'No')
