N = int(input())

x = 2025 - N
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == x:
            print(i, 'x', j)
