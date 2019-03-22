N = list(map(int, input().split()))
N.sort()

if N[1] == 1:
    print(1)
elif N[0] == 1:
    print(N[1] - 2)
else:
    print((N[0] - 2) * (N[1] - 2))
