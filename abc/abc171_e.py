from functools import reduce

N = int(input())
a = list(map(int, input().split()))

X = reduce(lambda x, y: x ^ y, a)
ans = [ai ^ X for ai in a]
print(' '.join(list(map(str, ans))))
