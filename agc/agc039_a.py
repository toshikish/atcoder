S = input()
K = int(input())

ans = 0
len_S = len(S)
a = b = 0
c = 1
same_letter = True
for i in range(len_S - 1):
    if S[i] == S[i + 1]:
        c += 1
    else:
        same_letter = False
        ans += c // 2
        if i == c - 1:
            a = c
        c = 1
b = c
ans += c // 2
if same_letter:
    ans = len_S * K // 2
else:
    ans *= K
    if S[0] == S[-1] and K >= 2 and (a % 2) * (b % 2) == 1:
        ans += K - 1
print(ans)
