N = int(input())
A = list(map(int, input().split()))

R = A[:]
for i in range(N - 1, -1, -1):
    R[i] = R[i + 1] + A[i]
B = 1
ans = B
for i in range(1, N + 1):
    M = 2 * B - A[i]
    if M < 0:
        ans = -1
        break
    B = min(M, max(0, R[i] - A[i]))
    ans += A[i] + B

print(ans if A[0] == 0 or A[0] == 1 and len(A) == 1 else -1)
