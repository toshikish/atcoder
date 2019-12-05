s = input()

possible = True
N = len(s)
for i in range(N // 2):
    if s[i] != s[N - i - 1] and s[i] != '*' and s[N - i - 1] != '*':
        possible = False
        break
print('YES' if possible else 'NO')
