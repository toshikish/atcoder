A, B, K = map(int, input().split())
k = max(K - A, 0)
print(max(A - K, 0), max(B - k, 0))
