import bisect

n = int(input())
a = list(map(int, input().split()))

a.sort()
ai = a.pop()
i = bisect.bisect_left(a, ai / 2)
if i == 0:
    aj = a[0]
elif i == n - 1:
    aj = a[n - 2]
else:
    aj = a[i - 1] if ai / 2 - a[i - 1] <= a[i] - ai / 2 else a[i]

print(ai, aj)
