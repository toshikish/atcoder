N = int(input())

if N % 111 == 0:
    print(N)
else:
    print((int(N / 111) + 1) * 111)
