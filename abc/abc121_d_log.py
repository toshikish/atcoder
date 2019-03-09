A, B = map(int, input().split())

def calcXorSum(a):
    bin_a = format(a, 'b')
    N = len(bin_a)
    a += 1
    ans = 0
    for i in range(N):
        unit = 1 << i
        div = int(a / unit)
        res = int(a % unit)
        cnt = unit * int(div / 2)
        if div % 2 == 1:
            cnt += res
        if cnt % 2 == 1:
            ans += 1 << i
    return ans

print(calcXorSum(B) ^ calcXorSum(A - 1))
