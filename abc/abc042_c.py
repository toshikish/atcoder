N, K = map(int, input().split())
D = list(map(int, input().split()))

ans = N
while True:
    tmp = ans
    finish = True
    while tmp > 0:
        if tmp % 10 in D:
            finish = False
            break
        tmp //= 10
    if finish:
        break
    ans += 1
print(ans)
