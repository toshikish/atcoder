n = int(input())
a = list(map(int, input().split()))

b = []
for i in range(n, 0, -2):
    b.append(str(a[i - 1]))
for i in range(1 if n % 2 == 0 else 2, n, 2):
    b.append(str(a[i - 1]))
print(' '.join(b))
