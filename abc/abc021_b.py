N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))

visited = [False] * N
visited[a - 1] = visited[b - 1] = True
ans = True
for p in P:
    if visited[p - 1]:
        ans = False
        break
    visited[p - 1] = True
print('YES' if ans else 'NO')
