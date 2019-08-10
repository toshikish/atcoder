K, X = map(int, input().split())

x_min = max(X - K + 1, -1000000)
x_max = min(X + K - 1, 100000)

L = map(str, list(range(x_min, x_max + 1)))
print(' '.join(L))
