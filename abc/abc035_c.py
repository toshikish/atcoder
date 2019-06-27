N, Q = map(int, input().split())
a = [0] * N
for i in range(Q):
    li, ri = map(int, input().split())
    a[li - 1] += 1
    if ri < N:
        a[ri] -= 1
b = [a[0] % 2]
for i in range(1, N):
    b.append((b[-1] + a[i]) % 2)
print(''.join([str(bi) for bi in b]))
