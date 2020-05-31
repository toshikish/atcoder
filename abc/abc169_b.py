N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    ans = 0
else:
    ans = 1
    for Ai in A:
        ans *= Ai
        if ans > 10 ** 18:
            ans = -1
            break
print(ans)
