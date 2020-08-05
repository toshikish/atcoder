N = int(input())
R = []
B = []
for i in range(N):
    Xi, Ci = input().split()
    if Ci == 'R':
        R.append(int(Xi))
    else:
        B.append(int(Xi))

R.sort()
B.sort()
for x in R + B:
    print(x)
