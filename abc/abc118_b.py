N, M = map(int, input().rstrip().split())
K = []
A = []
likes = [0] * M
for i in range(N):
    KA = list(map(int, input().rstrip().split()))
    for j in KA[1:]:
        likes[j - 1] += 1

print(likes.count(N))
