N = int(input())
X = list(map(int, input().split()))

sorted_X = sorted(X)
left = sorted_X[N // 2 - 1]
right = sorted_X[N // 2]

for x in X:
    print(right if x <= left else left)
