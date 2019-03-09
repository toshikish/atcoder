N, M, C = map(int, input().split())
B = list(map(int, input().split()))

cnt = 0
for i in range(N):
    A = list(map(int, input().split()))
    s = sum([A[j] * B[j] for j in range(M)])
    s += C
    if s > 0:
        cnt += 1
print(cnt)
