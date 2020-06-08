from collections import defaultdict, deque

N = int(input())
X = defaultdict(list)
for i in range(N - 1):
    ai, bi = map(lambda s: int(s) - 1, input().split())
    X[ai].append(bi)
    X[bi].append(ai)
c = list(map(int, input().split()))

c.sort(reverse=True)
print(sum(c[1:]))
d = [0] * N
q = deque([0])
i = 0
while len(q) > 0:
    v = q.popleft()
    d[v] = c[i]
    i += 1
    for x in X[v]:
        if d[x] != 0:
            continue
        q.append(x)
print(' '.join(list(map(str, d))))
