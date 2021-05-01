from collections import deque

S = input()

q = deque()
flipped = False
for Si in S:
    if Si == 'R':
        flipped = not flipped
    else:
        if flipped:
            if q and q[0] == Si:
                q.popleft()
            else:
                q.appendleft(Si)
        else:
            if q and q[-1] == Si:
                q.pop()
            else:
                q.append(Si)

T = list(q)
if flipped:
    T = T[::-1]
print(''.join(T))
