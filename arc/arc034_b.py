N = int(input())


def f(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


A = []
for x in range(max(N - 153, 1), N):
    if x + f(x) == N:
        A.append(x)

print(len(A))
for Ai in A:
    print(Ai)
