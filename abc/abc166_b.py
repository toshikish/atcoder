N, K = map(int, input().split())
A = []
for i in range(K):
    di = int(input())
    Ai = list(map(int, input().split()))
    A.extend(Ai)

print(N - len(set(A)))
