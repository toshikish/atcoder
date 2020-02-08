N, va, vb, L = map(int, input().split())

d = L
for i in range(N):
    t = d / va
    d = t * vb
print('{:.12f}'.format(d))
