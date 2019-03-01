N, T = map(int, input().split())
C = []
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        C.append(c)

if C == []:
    print('TLE')
else:
    print(min(C))
