N = int(input())
a = list(map(int, input().split()))

K = 0
for ai in a:
    if ai == K + 1:
        K += 1
print(N - K if K > 0 else -1)
