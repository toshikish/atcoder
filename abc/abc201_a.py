A = list(map(int, input().split()))
A.sort()
print('Yes' if A[0] + A[2] == A[1] * 2 else 'No')
