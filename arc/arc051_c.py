K = int(input())

a = b = 1
for i in range(K - 1):
    a, b = b, a + b
print(a, b)
