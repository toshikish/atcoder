N, K = map(int, input().split())
A = list(map(int, input().split()))


def C(x):
    return sum([max((Ai + x - 1) // x - 1, 0) for Ai in A])


A.sort()
left = 1
right = A[-1]
while left + 1 < right:
    mid = (left + right) // 2
    S = C(mid)
    if S <= K:
        right = mid
    else:
        left = mid
print(left if C(left) <= K else right)
