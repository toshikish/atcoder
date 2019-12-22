from collections import defaultdict, deque

N, u, v = map(int, input().split())
u -= 1
v -= 1
adj = defaultdict(list)
for i in range(N - 1):
    Ai, Bi = map(lambda x: int(x) - 1, input().split())
    adj[Ai].append(Bi)
    adj[Bi].append(Ai)

A = [0] * N
stack = deque()
stack.append(v)
while len(stack) > 0:
    e = stack.popleft()
    for a in adj[e]:
        if a == v or A[a] != 0:
            continue
        A[a] = A[e] + 1
        stack.append(a)

T = [0] * N
stack = deque()
stack.append(u)
while len(stack) > 0:
    e = stack.popleft()
    for a in adj[e]:
        if a == u or T[a] != 0 or A[a] < T[e] + 1:
            continue
        T[a] = T[e] + 1
        stack.append(a)

print(max([A[i] for i in range(N) if T[i] != 0 or i == u]) - 1)
