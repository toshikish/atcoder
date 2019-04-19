N, K = map(int, input().split())
A = list(map(int, input().split()))
print((N - 1) // (K - 1) + (1 if (N - 1) % (K - 1) != 0 else 0))
