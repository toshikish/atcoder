S, T = input(), input()
conv_table = {}
inv_table = {}

able = True
for i in range(len(S)):
    if S[i] in conv_table:
        if conv_table[S[i]] != T[i]:
            able = False
            break
    else:
        conv_table[S[i]] = T[i]
    if T[i] in inv_table:
        if inv_table[T[i]] != S[i]:
            able = False
            break
    else:
        inv_table[T[i]] = S[i]
print('Yes' if able else 'No')
