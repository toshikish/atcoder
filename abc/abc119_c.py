N, A, B, C = list(map(int, input().rstrip().split()))
l = [int(input()) for i in range(N)]

costs = []

for i in range(2 ** (2 * N)):
    i_bin = format(i, '0' + str(2 * N) + 'b')
    cost = 0
    a = b = c = 0
    for j in range(N):
        t = i_bin[j * 2 : j * 2 + 2]
        if t == '01':
            cost += 10
            a += l[j]
        elif t == '10':
            cost += 10
            b += l[j]
        elif t == '11':
            cost += 10
            c += l[j]
    if min(a, b, c) == 0:
        continue
    cost += abs(a - A) + abs(b - B) + abs(c - C) - 30
    costs.append(cost)

print(min(costs))