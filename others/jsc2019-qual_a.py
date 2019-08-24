M, D = map(int, input().split())

ans = 0
for d in range(1, D + 1):
    d_1 = d % 10
    d_10 = d // 10
    if d_1 < 2 or d_10 < 2:
        continue
    m = d_1 * d_10
    if m <= M:
        ans += 1
print(ans)
