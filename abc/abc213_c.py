H, W, N = map(int, input().split())
A = []
B = []
for i in range(N):
    Ai, Bi = map(int, input().split())
    A.append((Ai, i))
    B.append((Bi, i))

A.sort()
C = [0] * N
t = 0
for i in range(N):
    if i == 0 or A[i][0] != A[i - 1][0]:
        t += 1
    C[A[i][1]] = t
B.sort()
D = [0] * N
t = 0
for i in range(N):
    if i == 0 or B[i][0] != B[i - 1][0]:
        t += 1
    D[B[i][1]] = t

for i in range(N):
    print(C[i], D[i])
