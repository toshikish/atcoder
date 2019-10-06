N = int(input())
A = list(set(int(input()) for i in range(N)))

A.sort()
print(A[-2])
