from itertools import permutations

N, M = map(int, input().split())
T = [[False] * N for _ in range(N)]
for _ in range(M):
    Ai, Bi = map(lambda s: int(s) - 1, input().split())
    T[Ai][Bi] = T[Bi][Ai] = True
A = [[False] * N for _ in range(N)]
for _ in range(M):
    Ci, Di = map(lambda s: int(s) - 1, input().split())
    A[Ci][Di] = A[Di][Ci] = True

ans = False
for P in permutations(range(N)):
    if all(T[i][j] == A[P[i]][P[j]] for i in range(N) for j in range(N)):
        ans = True
        break
print('Yes' if ans else 'No')
