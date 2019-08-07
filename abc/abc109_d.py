H, W = map(int, input().split())
a = [list(map(int, input().split())) for i in range(H)]


def next(h, w):
    if h % 2 == 0:
        if w == W - 1:
            return (h + 1, w)
        else:
            return (h, w + 1)
    else:
        if w == 0:
            return (h + 1, w)
        else:
            return (h, w - 1)


ans = []
for i in range(H):
    for j in range(W):
        if i == H - 1 and j == W - 1:
            break
        if i % 2 == 0:
            h, w = i, j
        else:
            h, w = i, W - 1 - j
        if a[h][w] % 2 == 1:
            hn, wn = next(h, w)
            a[h][w] -= 1
            a[hn][wn] += 1
            ans.append("{} {} {} {}".format(h + 1, w + 1, hn + 1, wn + 1))
    else:
        continue
    break
print(len(ans))
for ai in ans:
    print(ai)
