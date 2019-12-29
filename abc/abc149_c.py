X = int(input())

if X == 2:
    ans = X
else:
    d = X + 1 if X % 2 == 0 else X
    while True:
        i = 3
        while i * i <= d:
            if d % i == 0:
                break
            i += 2
        else:
            ans = d
            break
        d += 2

print(ans)
