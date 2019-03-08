N = int(input())

able = False
for i in range(int(N / 4) + 1):
    for j in range(int(N / 7) + 1):
        if 4 * i + 7 * j == N:
            able = True
print('Yes' if able else 'No')
