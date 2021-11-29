N, X = map(int, input().split())
X -= 1
A = list(map(lambda s: int(s) - 1, input().split()))

knows = [False] * N
knows[X] = True
i = X
while True:
    i = A[i]
    if knows[i]:
        break
    knows[i] = True
print(knows.count(True))
