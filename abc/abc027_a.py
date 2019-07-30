l = list(map(int, input().split()))
l.sort()
print(l[0] if l[1] == l[2] else l[2])
