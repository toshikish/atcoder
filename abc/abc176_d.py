from collections import deque

H, W = map(int, input().split())
Ch, Cw = map(lambda s: int(s) - 1, input().split())
Dh, Dw = map(lambda s: int(s) - 1, input().split())
S = [input() for i in range(H)]

N = [[1000000007] * W for i in range(H)]
visited = [[False] * W for i in range(H)]
q = deque([(Ch, Cw)])
N[Ch][Cw] = 0
while len(q) > 0:
    ph, pw = q.popleft()
    if visited[ph][pw]:
        continue
    visited[ph][pw] = True
    for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nh = ph + dh
        nw = pw + dw
        if not 0 <= nh < H or not 0 <= nw < W or S[nh][nw] == '#':
            continue
        N[nh][nw] = min(N[nh][nw], N[ph][pw])
        if not visited[nh][nw]:
            q.appendleft((nh, nw))
    for dh in range(-2, 3):
        nh = ph + dh
        if not 0 <= nh < H:
            continue
        for dw in range(-2, 3):
            nw = pw + dw
            if not 0 <= nw < W or S[nh][nw] == '#':
                continue
            N[nh][nw] = min(N[nh][nw], N[ph][pw] + 1)
            if not visited[nh][nw]:
                q.append((nh, nw))

print(N[Dh][Dw] if visited[Dh][Dw] else -1)
