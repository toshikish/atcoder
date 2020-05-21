from bisect import bisect_left

N = int(input())
w = [int(input()) for i in range(N)]

s = []
for wi in w:
    i = bisect_left(s, wi)
    if i == len(s):
        s.append(wi)
    else:
        s[i] = wi
print(len(s))
