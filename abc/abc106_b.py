N = int(input())

cnt = 0
for n in range(1, N + 1, 2):
    n_div = 0
    for i in range(1, n + 1):
        if n % i == 0:
            n_div += 1
    if n_div == 8:
        cnt += 1

print(cnt)
