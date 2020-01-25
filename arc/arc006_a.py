E = list(map(int, input().split()))
B = int(input())
L = list(map(int, input().split()))

c = 0
bonus = False
j = 0
for i in range(6):
    while j < 6 and E[j] <= L[i]:
        if E[j] == L[i]:
            c += 1
            j += 1
            break
        j += 1
    if L[i] == B:
        bonus = True

d = {6: 1, 5: 3, 4: 4, 3: 5, 2: 0, 1: 0, 0: 0}
ans = d[c]
if ans == 3 and bonus:
    ans = 2
print(ans)
