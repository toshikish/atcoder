N, M, A, B = map(int, input().split())
c = [int(input()) for i in range(M)]

for i in range(M):
    if N <= A:
        N += B
    N -= c[i]
    if N < 0:
        ans = i + 1
        break
else:
    ans = 'complete'
print(ans)
