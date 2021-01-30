N = int(input())

NN = 2 * N
i = 1
ans = 0
while i * i <= NN:
    if NN % i != 0:
        i += 1
        continue
    m, n = i, NN // i
    if (m - n) % 2 == 1:
        ans += 1 if m == n else 2
    i += 1
print(ans)
