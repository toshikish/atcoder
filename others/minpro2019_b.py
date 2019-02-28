import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

counter = [0] * 4
for i in range(3):
    a, b = map(int, input().rstrip().split())
    counter[a - 1] += 1
    counter[b - 1] += 1
if compare(counter, [1, 1, 2, 2]):
    print('YES')
else:
    print('NO')