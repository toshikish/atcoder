T = int(input())
MOD = 1_000_000_007
for _ in range(T):
    N, A, B = map(int, input().split())
    if A + B >= N + 1:
        print(0)
        continue
    sq = (N - A - B + 1) * (N - A - B + 2) // 2 % MOD
    ans = (N - A + 1) * (N - B + 1) * sq - sq * sq
    print(ans * 4 % MOD)
