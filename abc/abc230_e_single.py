N = int(input())

ans = 0
i = 1
while i <= N:
    d = N // i
    ni = N // d + 1
    ans += d * (ni - i)
    i = ni

print(ans)
