x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

print('NO' if x2 + r <= x1 <= x3 - r and y2 + r <= y1 <= y3 - r else 'YES')
blue = False
for x in [x2, x3]:
    for y in [y2, y3]:
        if (x - x1) ** 2 + (y - y1) ** 2 > r ** 2:
            blue = True
            break
print('YES' if blue else 'NO')
