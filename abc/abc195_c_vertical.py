N = int(input())

ans = 0
b = 1000
while N >= b:
    ans += N - b + 1
    b *= 1000
print(ans)
