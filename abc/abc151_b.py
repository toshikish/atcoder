N, K, M = map(int, input().split())
A = list(map(int, input().split()))

d = max(N * M - sum(A), 0)
print(d if d <= K else -1)
