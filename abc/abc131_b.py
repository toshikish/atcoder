N, L = map(int, input().split())
if L > 0:
    m = L
elif L + N - 1 < 0:
    m = L + N - 1
else:
    m = 0
print((L - 1) * N + N * (N + 1) // 2 - m)
