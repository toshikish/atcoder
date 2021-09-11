from collections import deque
from heapq import heappush, heappop

Q = int(input())
A = []
B = deque()
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        B.append(query[1])
    elif query[0] == 2:
        if A:
            ans = heappop(A)
        else:
            ans = B.popleft()
        print(ans)
    else:
        while B:
            heappush(A, B.popleft())
