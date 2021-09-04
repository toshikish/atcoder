from collections import deque

N, M = map(int, input().split())
k = [0] * M
a = [[] for _ in range(M)]
for i in range(M):
    k[i] = int(input())
    a[i] = list(map(lambda s: int(s) - 1, input().split()))

index = [0] * M
position = [-1] * N
q = deque(list(range(M)))
while q:
    cy = q.popleft()
    cl = a[cy][index[cy]]
    pcl = position[cl]
    if pcl == -1:
        position[cl] = cy
    else:
        index[cy] += 1
        if index[cy] < k[cy]:
            q.append(cy)
        index[pcl] += 1
        if index[pcl] < k[pcl]:
            q.append(pcl)
        position[cl] = -1

print('Yes' if all(index[i] == k[i] for i in range(M)) else 'No')
