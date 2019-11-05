H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))

b = []
for i in range(N):
    b.extend([i + 1] * a[i])

for i in range(H):
    row = b[i * W:(i + 1) * W]
    if i % 2 == 1:
        row.reverse()
    print(' '.join([str(c) for c in row]))
