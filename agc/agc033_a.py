from collections import deque

H, W = map(int, input().split())
A = [list(input()) for i in range(H)]

q = deque()
for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            q.append((i, j))

ans = 0
while q:
    nq = deque()
    while q:
        h, w = q.popleft()
        if h > 0 and A[h - 1][w] == '.':
            A[h - 1][w] = '#'
            nq.append((h - 1, w))
        if h < H - 1 and A[h + 1][w] == '.':
            A[h + 1][w] = '#'
            nq.append((h + 1, w))
        if w > 0 and A[h][w - 1] == '.':
            A[h][w - 1] = '#'
            nq.append((h, w - 1))
        if w < W - 1 and A[h][w + 1] == '.':
            A[h][w + 1] = '#'
            nq.append((h, w + 1))
    if not nq:
        break
    q = nq
    ans += 1
print(ans)
