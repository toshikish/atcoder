N = int(input())

for h in range(1, 3501):
    for n in range(1, 3501):
        num = N * h * n
        denom = 4 * h * n - N * n - N * h
        if denom > 0 and num % denom == 0:
            w = num // denom
            break
    else:
        continue
    break
print(h, n, w)
