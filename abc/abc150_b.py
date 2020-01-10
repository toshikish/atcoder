N = int(input())
S = input()

ans = 0
c = 0
for s in S:
    if s == 'A':
        c = 1
    elif s == 'B' and c == 1:
        c = 2
    elif s == 'C' and c == 2:
        c = 0
        ans += 1
    else:
        c = 0
print(ans)
