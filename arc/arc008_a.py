N = int(input())
print(min(100 * (N // 10) + 15 * (N % 10), 100 * ((N + 10 - 1) // 10)))
