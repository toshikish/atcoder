N = int(input())
A = list(map(int, input().split()))

A.sort()
a = 0
failed = 0
for i in range(N - 1):
    a += A[i]
    if A[i + 1] > 2 * a:
        failed = i + 1
print(N - failed)
