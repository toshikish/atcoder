N, M = map(int, input().split())
H = list(map(int, input().split()))

F = [True] * N
for i in range(M):
    Ai, Bi = map(lambda s: int(s) - 1, input().split())
    if H[Ai] > H[Bi]:
        F[Bi] = False
    elif H[Ai] < H[Bi]:
        F[Ai] = False
    else:
        F[Ai] = F[Bi] = False

print(F.count(True))
