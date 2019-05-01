from collections import defaultdict

N, W = map(int, input().split())

MAX_NUM = []
len_weights = 0
def dfs(nums):
    if len(nums) == len_weights:
        sum_w = 0
        value = 0
        for i in range(len_weights):
            sum_w += weights[i] * nums[i]
            if nums[i] >= 1:
                value += items[weights[i]][nums[i] - 1]
        return value if sum_w <= W else 0
    value = 0
    for i in range(MAX_NUM[len(nums)] + 1):
        value = max(value, dfs(nums + [i]))
    return value

items = defaultdict(list)
for i in range(N):
    w, v = map(int, input().split())
    items[w].append(v)

for v in items.values():
    v.sort(reverse=True)
    for i in range(1, len(v)):
        v[i] = v[i - 1] + v[i]

weights = sorted(items.keys())
len_weights = len(weights)
for w in weights:
    MAX_NUM.append(min(W // w, len(items[w])))
print(dfs([]))
