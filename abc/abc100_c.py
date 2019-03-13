N = int(input())
a = list(map(int, input().split()))

cnt = 0
for ai in a:
    while ai % 2 == 0:
        ai //= 2
        cnt += 1
print(cnt)
