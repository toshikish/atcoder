a = list(map(int, input().split()))
a.sort()
print(a[2] if a[0] == a[1] else a[0] if a[1] == a[2] else 0)
