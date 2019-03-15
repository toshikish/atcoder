N = int(input())

P = [0]
n = 6
while n <= 100000:
    P.append(n)
    n *= 6
n = 9
while n <= 100000:
    P.append(n)
    n *= 9

def dp(n):
    amount = max(list(filter(lambda x: x <= n, P)))
    if amount == 0:
        return n
    return 1 + dp(n - amount)

print(dp(N))
