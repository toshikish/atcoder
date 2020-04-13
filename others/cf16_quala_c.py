s = list(input())
K = int(input())

for i in range(len(s)):
    if s[i] == 'a':
        continue
    n = ord('z') - ord(s[i]) + 1
    if n <= K:
        K -= n
        s[i] = 'a'

K %= 26
s[-1] = chr((ord(s[-1]) - ord('a') + K) % 26 + ord('a'))

print(''.join(s))
