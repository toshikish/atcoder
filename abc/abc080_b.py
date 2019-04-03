N = int(input())

x = N
f = 0
while x != 0:
    f += x % 10
    x //= 10
print('Yes' if N % f == 0 else 'No')
