N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = True
a = b = True
for i in range(1, N):
    na = a and abs(A[i - 1] - A[i]) <= K or b and abs(B[i - 1] - A[i]) <= K
    nb = a and abs(A[i - 1] - B[i]) <= K or b and abs(B[i - 1] - B[i]) <= K
    if not na and not nb:
        ans = False
        break
    a, b = na, nb

print('Yes' if ans else 'No')
