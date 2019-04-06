N = int(input())
A = [int(input()) for i in range(5)]

m = min(A)
t = N // m
if N % m != 0:
    t += 1
print(t + 4)
