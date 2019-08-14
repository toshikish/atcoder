from collections import defaultdict

N = int(input())
balloons = [tuple(map(int, input().split())) for i in range(N)]


def judge(x):
    d = defaultdict(int)
    for h, s in balloons:
        t = (x - h) // s
        d[t] += 1
    c = 0
    for i in range(N):
        c += d[i]
        if c > i + 1:
            return False
    return True


max_H = 0
max_HSN = 0
for H, S in balloons:
    max_H = max(H, max_H)
    max_HSN = max(H + S * (N - 1), max_HSN)

left = max_H - 1
right = max_HSN
while left < right - 1:
    mid = (left + right) // 2
    if judge(mid):
        right = mid
    else:
        left = mid
print(right)
