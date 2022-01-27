X, Y = map(int, input().split())
print((max(Y - X, 0) + 10 - 1) // 10)
