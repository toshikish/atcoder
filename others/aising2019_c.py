from collections import deque, defaultdict

H, W = map(int, input().split())
S = [input() for i in range(H)]

visited = [[False] * W for i in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if visited[i][j]:
            continue
        q = deque()
        q.append((i, j))
        visited[i][j] = True
        n = defaultdict(int)
        while len(q) > 0:
            si, sj = q.popleft()
            n[S[si][sj]] += 1
            for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if 0 <= si + di < H and 0 <= sj + dj < W and S[si][sj] != S[si + di][sj + dj] and not visited[si + di][sj + dj]:
                    q.append((si + di, sj + dj))
                    visited[si + di][sj + dj] = True
        ans += n['#'] * n['.']

print(ans)
