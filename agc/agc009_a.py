N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
	A[i], B[i] = map(int, input().split())

ans = 0
for i in range(N - 1, -1, -1):
    a = (A[i] + ans) % B[i]
    if a > 0:
    	ans += B[i] - a
print(ans)
