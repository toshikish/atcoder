N = int(input())
visited = set()
ans = 0
for i in range(N):
    A = int(input())
    if A in visited:
        ans += 1
    else:
        visited.add(A)
print(ans)
