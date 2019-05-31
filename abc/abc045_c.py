S = input()

N = len(S)
ans = 0
for i in range(2 ** (N - 1)):
    bit = '{:010b}'.format(i)[11 - N:]
    formula = S[0]
    for j in range(len(bit)):
        if bit[j] == '1':
            formula += '+'
        formula += S[j + 1]
    ans += eval(formula)
print(ans)
