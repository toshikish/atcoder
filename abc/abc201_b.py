N = int(input())
mountains = []
for _ in range(N):
    Si, Ti = input().split()
    mountains.append((int(Ti), Si))

mountains.sort(reverse=True)
print(mountains[1][1])
