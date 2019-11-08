A, B, K, L = map(int, input().split())
print(B * (K // L) + min(A * (K % L), B))
