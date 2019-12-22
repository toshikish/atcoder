N = int(input())

ans = 0
if N % 2 == 0:
    d = 10
    while N >= d:
        ans += N // d
        d *= 5
print(ans)
