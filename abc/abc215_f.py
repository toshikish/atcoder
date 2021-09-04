N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

P.sort()


def f(d):
    j = 0
    ly = 1_000_000_001
    ry = -1
    for i in range(N):
        while j < i and P[j][0] <= P[i][0] - d:
            ly = min(ly, P[j][1])
            ry = max(ry, P[j][1])
            j += 1
        if ly <= P[i][1] - d or ry >= P[i][1] + d:
            return True
    return False


low = 0
high = 1000_000_001
while low + 1 < high:
    mid = (low + high) // 2
    if f(mid):
        low = mid
    else:
        high = mid

print(low)
