S = input()

s1 = 1 <= int(S[0:2]) <= 12
s2 = 1 <= int(S[2:4]) <= 12
if s1 and s2:
    ans = 'AMBIGUOUS'
elif s1:
    ans = 'MMYY'
elif s2:
    ans = 'YYMM'
else:
    ans = 'NA'
print(ans)
