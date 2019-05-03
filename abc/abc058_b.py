O = input()
E = input()
P = []
for i in range(1, len(O) + len(E) + 1):
    if i % 2 == 0:
        P.append(E[i // 2 - 1])
    else:
        P.append(O[i // 2])
print(''.join(P))
