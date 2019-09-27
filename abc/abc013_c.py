N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

res = E * N - H
if res <= 0:
    ans = 0
else:
    ans = A * N
    for i in range(N + 1):
        r = res - (B + E) * i + 1
        j = max(0, (r + D + E - 1) // (D + E))
        if i + j > N:
            continue
        ans = min(ans, A * i + C * j)
        if j == 0:
            break
print(ans)
