N, K = map(int, input().split())
h = [int(input()) for i in range(N)]

h.sort()
min_diff = 10 ** 10
for i in range(N - K + 1):
    diff = h[i + K - 1] - h[i]
    if diff < min_diff:
        min_diff = diff
print(min_diff)