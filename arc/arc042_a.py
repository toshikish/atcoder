N, M = map(int, input().split())
a = [int(input()) - 1 for i in range(M)]

updated = [False] * N
t = []
for i in range(M - 1, -1, -1):
    if not updated[a[i]]:
        updated[a[i]] = True
        t.append(a[i])

for i in range(N):
    if not updated[i]:
        t.append(i)

for i in range(N):
    print(t[i] + 1)
