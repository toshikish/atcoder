from math import factorial

N, P = map(int, input().split())
A = list(map(lambda x: int(x) % 2, input().split()))

n0 = A.count(0)
n1 = A.count(1)
ans0 = 2 ** n0
ans1 = 0
for i in range(P, n1 + 1, 2):
    ans1 += factorial(n1) // (factorial(i) * factorial(n1 - i))
print(ans0 * ans1)
