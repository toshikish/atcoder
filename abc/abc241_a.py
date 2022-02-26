a = list(map(int, input().split()))
x = a[0]
for _ in range(2):
    x = a[x]
print(x)
