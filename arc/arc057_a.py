A, K = map(int, input().split())
MAX = 2 * 10 ** 12

if K == 0:
    ans = MAX - A
else:
    ans = 0
    money = A
    while money < MAX:
        money = 1 + (K + 1) * money
        ans += 1
print(ans)
