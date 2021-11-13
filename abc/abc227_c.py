N = int(input())

ans = 0
a = 1
while a * a * a <= N:
    b = a
    while b * b <= N:
        c = N // (a * b)
        if b > c:
            break
        ans += c - b + 1
        b += 1
    a += 1
print(ans)
