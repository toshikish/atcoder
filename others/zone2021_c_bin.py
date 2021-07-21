from itertools import combinations_with_replacement

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]


def check(x):
    S = set()
    for Ai in A:
        S.add(sum(1 << i for i in range(5) if Ai[i] >= x))
    for c1, c2, c3 in combinations_with_replacement(S, 3):
        if c1 | c2 | c3 == 31:
            return True
    return False


low = 1
high = 1_000_000_001
while high - low > 1:
    mid = (high + low) // 2
    if check(mid):
        low = mid
    else:
        high = mid

print(low)
