from collections import deque

N = int(input())
T = [0] * N
K = [0] * N
A = []
for i in range(N):
    Ai = list(map(int, input().split()))
    T[i] = Ai[0]
    K[i] = Ai[1]
    A.append([ai - 1 for ai in Ai[2:]])

ans = 0
acquired = [False] * N
q = deque([N - 1])
while q:
    i = q.pop()
    if acquired[i]:
        continue
    ans += T[i]
    acquired[i] = True
    for j in A[i]:
        if not acquired[j]:
            q.append(j)
print(ans)
