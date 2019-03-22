A, B = map(int, input().split())

ans = 0
for i in range(A, B + 1):
    if i // 10000 == i % 10 and (i // 1000) % 10 == (i // 10) % 10:
        ans += 1
print(ans)
