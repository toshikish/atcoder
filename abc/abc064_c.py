from collections import defaultdict

N = int(input())
a = list(map(int, input().split()))

counter = defaultdict(int)
for ai in a:
    counter[min(ai // 400, 8)] += 1
ans = 0
for i in range(8):
    if counter[i] > 0:
        ans += 1
if ans == 0:
    print(1, counter[8])
else:
    print(ans, ans + counter[8])
