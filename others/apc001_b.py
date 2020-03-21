N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

n = sum(b) - sum(a)
c = 0
for i in range(N):
    if a[i] < b[i]:
        c += (b[i] - a[i] + 2 - 1) // 2
print('Yes' if c <= n else 'No')
