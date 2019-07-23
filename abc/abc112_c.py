N = int(input())
learn = []
verify = []
for i in range(N):
    a = tuple(map(int, input().split()))
    if a[2] > 0 and learn == []:
        learn.append(a)
    else:
        verify.append(a)

for Cx in range(101):
    for Cy in range(101):
        H = learn[0][2] + abs(learn[0][0] - Cx) + abs(learn[0][1] - Cy)
        right = True
        for v in verify:
            if max(H - abs(v[0] - Cx) - abs(v[1] - Cy), 0) != v[2]:
                right = False
                break
        else:
            break
        continue
    else:
        continue
    break

print(Cx, Cy, H)
