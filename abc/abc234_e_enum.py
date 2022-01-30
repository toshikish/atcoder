X = int(input())

k = len(str(X))
ans = 0
while ans < X:
    for a in range(1, 10):
        for d in range(-9, 9):
            if not 0 <= a + (k - 1) * d <= 9:
                continue
            n = int(''.join(list(map(str, [a + i * d for i in range(k)]))))
            if n >= X:
                ans = n
                break
        else:
            continue
        break
    else:
        k += 1
        continue
    break

print(ans)
