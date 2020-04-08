K, T = map(int, input().split())
a = list(map(int, input().split()))

M = max(a)
print(max(M - 1 - (K - M), 0))
