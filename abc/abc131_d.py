from collections import defaultdict

N = int(input())
jobs = defaultdict(int)
for i in range(N):
    Ai, Bi = map(int, input().split())
    jobs[Bi] += Ai

acu = 0
able = True
for Bi in sorted(jobs.keys()):
    acu += jobs[Bi]
    if acu > Bi:
        able = False
        break

print('Yes' if able else 'No')
