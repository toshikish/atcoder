N = int(input())

S = set()

a = b = 2
while a * a <= N:
    n = a * a
    while n <= N:
        S.add(n)
        n *= a
    a += 1

print(N - len(S))
