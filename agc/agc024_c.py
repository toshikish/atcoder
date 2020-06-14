N = int(input())
A = [int(input()) for i in range(N)]
 
if A[0] == 0 and all(A[i + 1] - A[i] <= 1 for i in range(N - 1)):
    ans = A[N - 1]
    for i in range(N - 2, -1, -1):
        if A[i] != A[i + 1] - 1:
            ans += A[i]
else:
    ans = -1
 
print(ans)
