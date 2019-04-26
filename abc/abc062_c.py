H, W = map(int, input().split())

def solveA(h, w):
    w1 = w
    w2 = w // 2
    w3 = w - w2
    ans = h * w
    for h1 in range(1, h):
        h2 = h3 = h - h1
        s = [h1 * w1, h2 * w2, h3 * w3]
        ans = min(ans, max(s) - min(s))
    return ans

def solveB(h, w):
    if h % 3 == 0:
        return 0
    else:
        return w

ans = min(solveA(H, W), solveA(W, H), solveB(H, W), solveB(W, H))
print(ans)
