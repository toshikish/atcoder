N = int(input())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

ans = 1
c = [0, 0, 0]
for i in range(N):
    n = c.count(A[i])
    ans *= n
    ans %= MOD
    if n > 0:
        c[c.index(A[i])] += 1
print(ans)
