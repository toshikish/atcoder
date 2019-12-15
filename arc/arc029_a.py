N = int(input())
t = [int(input()) for i in range(N)]

S = sum(t)
ans = S
for i in range(1 << N):
    subtotal = 0
    for j in range(N):
        if i >> j & 1:
            subtotal += t[j]
    ans = min(ans, max(subtotal, S - subtotal))
print(ans)
