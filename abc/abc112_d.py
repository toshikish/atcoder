N, M = map(int, input().split())

i = 1
ans = 0
UL = M / N
while i * i <= M:
    if M % i == 0:
        j = M // i
        if i <= UL:
            ans = max(ans, i)
        if j <= UL:
            ans = max(ans, j)
    i += 1

print(ans)
