N, M = map(int, input().split())
A = list(map(int, input().split()))

pos = [[] for _ in range(N)]
for i in range(N):
    pos[A[i]].append(i)

ans = N
for i in range(N):
    posi = [-1] + pos[i] + [N]
    for j in range(len(posi) - 1):
        if posi[j + 1] - posi[j] - 1 >= M:
            ans = i
            break
    else:
        continue
    break

print(ans)
