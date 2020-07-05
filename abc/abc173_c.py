H, W, K = map(int, input().split())
C = [input() for i in range(H)]

ans = 0
for i in range(1 << H):
    for j in range(1 << W):
        c = 0
        for h in range(H):
            if i >> h & 1 == 1:
                continue
            for w in range(W):
                if j >> w & 1 == 1:
                    continue
                if C[h][w] == '#':
                    c += 1
        if c == K:
            ans += 1
print(ans)
