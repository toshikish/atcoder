N = int(input())
a = list(map(int, input().split()))

A = sum(a) / N
d = [abs(ai - A) for ai in a]
print(d.index(min(d)))
