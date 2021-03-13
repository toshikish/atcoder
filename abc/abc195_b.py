A, B, W = map(int, input().split())

W *= 1000
l = (W + B - 1) // B
u = W // A
if l > u:
    print('UNSATISFIABLE')
else:
    print(l, u)
