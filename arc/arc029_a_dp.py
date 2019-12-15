N = int(input())
t = [int(input()) for i in range(N)]

S = sum(t)
dp = 0
for i in range(N):
    dp |= dp << t[i]
    dp |= 1 << (t[i] - 1)

ans = (S + 1) // 2
res = dp >> ((S + 1) // 2 - 1)
while res & 1 == 0:
    res >>= 1
    ans += 1
print(ans)
