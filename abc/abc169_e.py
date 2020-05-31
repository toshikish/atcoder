N = int(input())
A = []
B = []
for i in range(N):
    Ai, Bi = map(int, input().split())
    A.append(Ai)
    B.append(Bi)

A.sort()
B.sort()
if N % 2 == 0:
    ans = sum(B[N // 2 - 1:N // 2 + 1]) - sum(A[N // 2 - 1:N // 2 + 1]) + 1
else:
    ans = B[N // 2] - A[N // 2] + 1
print(ans)
