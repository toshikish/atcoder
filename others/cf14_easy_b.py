n = int(input())
print((n - 1) % 20 + 1 if (n - 1) // 20 % 2 == 0 else 20 - (n - 1) % 20)
