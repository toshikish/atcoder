N, A, B = map(int, input().split())
x = 0
for i in range(N):
    s, d = input().split()
    d = int(d)
    if d < A:
        d = A
    elif d > B:
        d = B
    if s == 'West':
        d *= -1
    x += d
if x > 0:
    print('East', x)
elif x < 0:
    print('West', -x)
else:
    print(0)
