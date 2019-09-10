N = int(input())
A = list(map(int, input().split()))

ans = 1
sgn = 0
for i in range(1, N):
    if sgn == 0:
        if A[i] > A[i - 1]:
            sgn = 1
        elif A[i] < A[i - 1]:
            sgn = -1
    elif sgn == 1 and A[i] < A[i - 1] or sgn == -1 and A[i] > A[i - 1]:
        ans += 1
        sgn = 0
print(ans)
