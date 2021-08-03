N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
i = j = 0
ans = abs(A[i] - B[j])
while i < N and j < M:
    ans = min(ans, abs(A[i] - B[j]))
    if A[i] == B[j]:
        ans = 0
        break
    if A[i] < B[j]:
        i += 1
    else:
        j += 1
print(ans)
