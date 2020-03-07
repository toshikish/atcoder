N = int(input())

ans = 0
while N > 0:
    if N % 10 == 2:
        ans += 1
    N //= 10
print(ans)
