from collections import defaultdict
MOD = 10 ** 9 + 7

H, W, K = map(int, input().split())

fib = {-2: 0, -1: 1, 0: 1}
for i in range(1, W):
    fib[i] = fib[i - 1] + fib[i - 2]

dp = defaultdict(int)
dp[(0, 1)] = 1
for i in range(1, H + 1):
    for j in range(1, W + 1):
        dp[(i, j)] \
            = fib[j - 3] * fib[W - j - 1] * dp[(i - 1, j - 1)] \
            + fib[j - 2] * fib[W - j - 1] * dp[(i - 1, j)] \
            + fib[j - 2] * fib[W - j - 2] * dp[(i - 1, j + 1)]
        dp[(i, j)] %= MOD

print(dp[(H, K)])
