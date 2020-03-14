H, W = map(int, input().split())

ans = 0
if H == 1 or W == 1:
    ans = 1
elif W % 2 == 0:
    ans = W // 2 * H
else:
    e = (W + 1) // 2
    o = W // 2
    ans = (e + o) * (H // 2)
    if H % 2 == 1:
        ans += e
print(ans)
