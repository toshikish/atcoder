S = input()
T = input()

print([S[i] != T[i] for i in range(len(S))].count(True))
