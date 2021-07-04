P = int(input())

c = [1] * 10
for i in range(1, 10):
    c[i] *= c[i - 1] * (i + 1)

ans = 0
for i in range(9, -1, -1):
    ans += P // c[i]
    P %= c[i]

print(ans)
