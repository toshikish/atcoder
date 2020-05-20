N = int(input())
H = set()
for i in range(N):
    H.add(tuple(map(int, input().split('/'))))

days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m = 1
d = 1
D = 0
ans = 0
c = 0
s = 0
while m <= 12:
    A = D == 0 or D == 6
    B = s > 0
    C = (m, d) in H
    if A and C:
        c += 1
        s += 1
    elif A or C:
        c += 1
    elif B:
        c += 1
        s -= 1
    else:
        c = 0
    ans = max(c, ans)
    d += 1
    if d > days[m - 1]:
        m += 1
        d = 1
    D += 1
    D %= 7
print(ans)
