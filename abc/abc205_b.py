N = int(input())
A = list(map(int, input().split()))

A.sort()
print('Yes' if all([A[i] == i + 1 for i in range(N)]) else 'No')
