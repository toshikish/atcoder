N = int(input())

s = 0
while N > 0:
    s += N % 10
    N //= 10
print(10 if s == 1 else s)
