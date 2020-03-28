import bisect
import heapq

X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort()
q.sort()
r.sort()
m = A - X
n = B - Y
l = bisect.bisect_right(r, min(p[m], q[n]))
print(sum(list(heapq.merge(p[m:], q[n:], r[l:]))[-(X + Y):]))
