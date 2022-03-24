N = int(input())
M = 2 * N + 1

used = [False] * (M + 1)
cursor = 1
while cursor <= M:
    while used[cursor]:
        cursor += 1
    used[cursor] = True
    print(cursor)
    i = int(input())
    if i == 0:
        break
    used[i] = True
