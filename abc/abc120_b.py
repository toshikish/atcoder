import fractions

A, B, K = map(int, input().split())

gcd = fractions.gcd(A, B)
order = 0
for i in range(gcd, 0, -1):
    if gcd % i == 0:
        order += 1
        if order == K:
            print(i)
            break
