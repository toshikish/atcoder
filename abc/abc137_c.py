from collections import defaultdict

N = int(input())
words = defaultdict(int)
for i in range(N):
    s = list(input())
    s.sort()
    words[''.join(s)] += 1

ans = 0
for n in words.values():
    if n == 1:
        continue
    ans += n * (n - 1) // 2
print(ans)
