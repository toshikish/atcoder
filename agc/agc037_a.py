S = input()

K = 1
prev = S[0]
i = 1
len_S = len(S)
while i < len_S:
    K += 1
    if prev == S[i] or i == len_S - 2 and S[i] == S[i + 1]:
        prev = S[i:i + 2]
        i += 2
    else:
        prev = S[i]
        i += 1
print(K)
