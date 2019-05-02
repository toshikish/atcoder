n = int(input())
a = list(map(int, input().split()))

def calc(sgn):
    ans = 0
    sum = 0
    for ai in a:
        sum += ai
        sgn *= -1
        if sum == 0:
            ans += 1
            sum = sgn
        elif sum * sgn < 0:
            ans += abs(sum) + 1
            sum = sgn
    return ans

print(min(calc(1), calc(-1)))
