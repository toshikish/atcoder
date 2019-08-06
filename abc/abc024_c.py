N, D, K = map(int, input().split())
LR = [tuple(map(int, input().split())) for j in range(D)]
ST = [tuple(map(int, input().split())) for i in range(K)]

ans = []
for st in ST:
    current = st[0]
    for i in range(D):
        if LR[i][0] <= current <= LR[i][1]:
            if LR[i][0] <= st[1] <= LR[i][1]:
                break
            else:
                current = LR[i][1] if st[0] < st[1] else LR[i][0]
    ans.append(i + 1)

for a in ans:
    print(a)
