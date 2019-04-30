A, B, C = map(int, input().split())

ans = False
for i in range(A + 1):
    if (B * i + C) % A == 0:
        ans = True
        break
print('YES' if ans else 'NO')
