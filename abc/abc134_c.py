from collections import defaultdict

N = int(input())
A = [int(input()) for i in range(N)]

d = defaultdict(int)
for Ai in A:
    d[Ai] += 1

sorted_A = sorted(d.keys(), reverse=True)
for Ai in A:
    if Ai < sorted_A[0]:
        ans = sorted_A[0]
    else:
        ans = sorted_A[0] if d[sorted_A[0]] >= 2 else sorted_A[1]
    print(ans)
