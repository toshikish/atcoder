N = int(input())

able = False
for i in range(1, 10):
    q = N // i
    if q <= 9 and i * q == N:
        able = True
        break
print('Yes' if able else 'No')
