S = input()

for l in range(len(S) - 2, 0, -2):
    half_l = l // 2
    if S[0:half_l] == S[half_l:l]:
        break
print(l)
