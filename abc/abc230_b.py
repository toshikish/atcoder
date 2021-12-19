S = input()

A = list(map(len, S.split('o')))
N = len(A)
if N == 1:
    ans = A[0] <= 2
elif N == 2:
    ans = A[0] <= 2 and A[1] <= 2
else:
    ans = A[0] <= 2 and A[-1] <= 2 and all(A[i] == 2 for i in range(1, N - 1))
print('Yes' if ans else 'No')
