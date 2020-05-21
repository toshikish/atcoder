from itertools import permutations

n, c = map(int, input().split())
a = [int(input()) - 1 for i in range(n)]

m = n
for p in permutations(range(10), 2):
    m = min([a[i] != p[i % 2] for i in range(n)].count(True), m)
print(m * c)
