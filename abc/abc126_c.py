import math

N, K = map(int, input().split())

ans = 0
if K <= N:
    ans += N - K + 1
for i in range(1, min(K, N + 1)):
    ans += (1 / 2) ** math.ceil(math.log2(K / i))

ans /= N
print('{:.10f}'.format(ans))
