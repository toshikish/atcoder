N = int(input())

d = len(str(N))
if d % 2 == 0:
    hd = d // 2
    u = N // 10 ** hd
    l = N % 10 ** hd
    if u > l:
        ans = u - 1
    else:
        ans = u
else:
    ans = 10 ** (d // 2) - 1
print(ans)
