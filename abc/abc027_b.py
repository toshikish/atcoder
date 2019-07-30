N = int(input())
a = list(map(int, input().split()))

S = sum(a)
if S % N == 0:
    av = S // N
    left = 0
    ans = 0
    for i in range(N - 1):
        left += a[i]
        if left != av * (i + 1):
            ans += 1
else:
    ans = -1
print(ans)
