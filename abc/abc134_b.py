N, D = map(int, input().split())
r = 1 if N % (2 * D + 1) > 0 else 0
print(N // (2 * D + 1) + r)
