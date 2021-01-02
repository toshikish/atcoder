N = int(input())
P = [tuple(map(int, input().split())) for i in range(N)]

C = [2 * Ai + Bi for Ai, Bi in P]
C.sort(reverse=True)
t = sum([P[i][0] for i in range(N)])
for i in range(N):
    t -= C[i]
    if t < 0:
        break

print(i + 1)
