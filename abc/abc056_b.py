W, a, b = map(int, input().split())
if b + W < a:
    ans = a - (b + W)
elif b <= a + W:
    ans = 0
else:
    ans = b - (a + W)
print(ans)
