N, M = map(int, input().split())

accepted = [False] * N
temp_p = [0] * N
p = 0
for i in range(M):
    pi, Si = input().split()
    pi = int(pi) - 1
    if not accepted[pi]:
        if Si == 'AC':
            p += temp_p[pi]
            accepted[pi] = True
        else:
            temp_p[pi] += 1
print(accepted.count(True), p)
