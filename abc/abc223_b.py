S = input()

N = len(S)
SS = S + S
D = [SS[i:i + N] for i in range(N)]
D.sort()
print(D[0])
print(D[-1])
