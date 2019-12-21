L, R = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))

sl = [0] * 31
sr = [0] * 31
for li in l:
    sl[li - 10] += 1
for ri in r:
    sr[ri - 10] += 1
print(sum([min(sl[i], sr[i]) for i in range(31)]))
