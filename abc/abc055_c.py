N, M = map(int, input().split())
print(M // 2 if 2 * N > M else (2 * N + M) // 4)
