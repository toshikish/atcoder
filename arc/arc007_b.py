N, M = map(int, input().split())
disks = [int(input()) for i in range(M)]

T = list(range(N + 1))
c = 0
for i in range(M):
    new_c = disks[i]
    T[c], T[new_c] = T[new_c], T[c]
    c = new_c

M = [0] * (N + 1)
for i in range(N + 1):
    M[T[i]] = i

for i in range(1, N + 1):
    print(M[i])
