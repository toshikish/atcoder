s = input()

N = len(s)
a, b = -1, -1
if N == 2:
    if s[0] == s[1]:
        a, b = 1, 2
else:
    for i in range(N - 2):
        if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i + 2] == s[i]:
            a, b = i + 1, i + 3
            break
print(a, b)
