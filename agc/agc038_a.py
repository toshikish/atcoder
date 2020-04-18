H, W, A, B = map(int, input().split())

for i in range(H):
    z, o = ('0', '1') if i < B else ('1', '0')
    print(''.join([z] * A + [o] * (W - A)))
