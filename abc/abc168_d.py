from collections import defaultdict, deque

N, M = map(int, input().split())
X = defaultdict(list)
for i in range(M):
    Ai, Bi = map(lambda s: int(s) - 1, input().split())
    X[Ai].append(Bi)
    X[Bi].append(Ai)

V = [False] * N
P = [0] * N
A = [0] * N
Q = deque([0])
V[0] = True
while len(Q) > 0:
    r = Q.popleft()
    for nr in X[r]:
        if V[nr] == True:
            continue
        V[nr] = True
        P[nr] = P[r] + 1
        A[nr] = r + 1
        Q.append(nr)

print('Yes')
for i in range(1, N):
    print(A[i])
