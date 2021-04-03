from collections import deque

H, W, A, B = map(int, input().split())

HW = H * W
S = deque()
S.append((0, 0, A, B))
ans = 0
while S:
    i, used, a, b = S.pop()
    if i == HW:
        ans += 1
        continue
    if used >> i & 1:
        S.append((i + 1, used, a, b))
    used |= 1 << i
    if b:
        S.append((i + 1, used, a, b - 1))
    if a:
        if i % W <= W - 2 and not used & 1 << (i + 1):
            S.append((i + 1, used | 1 << (i + 1), a - 1, b))
        if i // W <= H - 2:
            S.append((i + 1, used | 1 << (i + W), a - 1, b))
print(ans)
