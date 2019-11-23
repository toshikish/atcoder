H, W, K = map(int, input().split())
s = [input() for i in range(H)]

n = [s[i].count('#') for i in range(H)]
ans = []
initial_row = H
k = 1
for i in range(H):
    if n[i] == 0:
        if i > initial_row:
            ans.append(ans[-1])
        else:
            ans.append([0] * W)
    else:
        if initial_row == H:
            initial_row = i
        row = []
        first_in_row = True
        for j in range(W):
            if s[i][j] == '.':
                row.append(k)
            else:
                if first_in_row:
                    first_in_row = False
                else:
                    k += 1
                row.append(k)
        ans.append(row)
        k += 1
for i in range(initial_row):
    ans[i] = ans[initial_row]

for i in range(H):
    print(' '.join([str(aij) for aij in ans[i]]))
