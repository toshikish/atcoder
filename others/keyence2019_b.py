import sys
import re
s = input()
k = 'keyence'
for i in range(8):
    if re.match(k[:i] + '[a-z]*' + k[i:], s):
        print('YES')
        sys.exit()
print('NO')
