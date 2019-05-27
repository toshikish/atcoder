N, K = map(int, input().split())
print(K if N == 1 else K * (K - 1) ** (N - 1))
