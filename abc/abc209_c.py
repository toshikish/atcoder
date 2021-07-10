N = int(input())
C = list(map(int, input().split()))
MOD = 1_000_000_007

C.sort()
ans = C[0]
for i in range(1, N):
    ans *= C[i] - i
    ans %= MOD
print(ans)
