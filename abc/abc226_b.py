N = int(input())
S = set()
for _ in range(N):
    A = list(map(int, input().split()))
    S.add(tuple(A[1:]))
print(len(S))
