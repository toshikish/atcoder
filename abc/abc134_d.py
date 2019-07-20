N = int(input())
a = list(map(int, input().split()))

if N % 2 == 0:
    k = N // 2
    x = [0] * k + a[k:]
    start = k
else:
    k = (N + 1) // 2
    x = [0] * (k - 1) + a[k - 1:]
    start = k - 1

for i in range(start, 0, -1):
    x[i - 1] = (sum(x[2 * i - 1::i]) + a[i - 1]) % 2

M = 0
b = []
for i in range(N):
    if x[i] == 1:
        M += 1
        b.append(str(i + 1))
print(M)
print(' '.join(b))
