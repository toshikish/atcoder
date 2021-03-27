from collections import defaultdict

H, W, A, B = map(int, input().split())

HW = H * W


def dfs(i, used, a, b):
    if i == HW:
        return 1
    if used >> i & 1:
        return dfs(i + 1, used, a, b)
    c = 0
    used |= 1 << i
    if b:
        c += dfs(i + 1, used, a, b - 1)
    if a:
        if i % W <= W - 2 and not used & 1 << (i + 1):
            c += dfs(i + 1, used | 1 << (i + 1), a - 1, b)
        if i // W <= H - 2:
            c += dfs(i + 1, used | 1 << (i + W), a - 1, b)
    return c


print(dfs(0, 0, A, B))
