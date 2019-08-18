from collections import defaultdict
from bisect import bisect_left

s = input()
t = input()

len_s = len(s)
indices = defaultdict(list)
for i in range(len_s):
    indices[s[i]].append(i + 1)

letters_s = set(indices.keys())
letters_t = set(t)
if letters_t <= letters_s:
    cycles = 0
    cur = 0
    for ti in t:
        index = bisect_left(indices[ti], cur + 1)
        if index == len(indices[ti]):
            cycles += 1
            cur = indices[ti][0]
        else:
            cur = indices[ti][index]
    ans = len_s * cycles + cur
else:
    ans = -1
print(ans)
