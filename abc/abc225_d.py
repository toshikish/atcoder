from collections import deque

N, Q = map(int, input().split())
queries = [list(map(lambda s: int(s) - 1, input().split())) for _ in range(Q)]

INF = N
front = [INF] * N
back = [INF] * N
for query in queries:
    if query[0] == 0:
        x, y = query[1:]
        back[x] = y
        front[y] = x
    elif query[0] == 1:
        x, y = query[1:]
        back[x] = INF
        front[y] = INF
    else:
        x = query[1]
        q = deque([x + 1])
        i = front[x]
        while i != INF:
            q.appendleft(i + 1)
            i = front[i]
        i = back[x]
        while i != INF:
            q.append(i + 1)
            i = back[i]
        print(' '.join(list(map(str, [len(q)] + list(q)))))
