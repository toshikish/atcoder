A, B, C, D = map(int, input().split())

ans = -1
d = C * D - B
if d > 0:
    ans = (A + d - 1) // d
print(ans)
