N = int(input())
c = [0] * 6
for i in range(N):
    M, m = map(float, input().split())
    if M >= 35:
        c[0] += 1
    elif M >= 30:
        c[1] += 1
    elif M >= 25:
        c[2] += 1
    if m >= 25:
        c[3] += 1
    elif m < 0 and M >= 0:
        c[4] += 1
    elif M < 0:
        c[5] += 1
print(' '.join(list(map(str, c))))
