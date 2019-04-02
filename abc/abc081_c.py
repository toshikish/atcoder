from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

counter = defaultdict(int)
for a in A:
    counter[a] += 1
n = list(counter.values())
n.sort(reverse=True)
print(sum(n[K:]))
