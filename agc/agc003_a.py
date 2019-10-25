from collections import Counter

S = input()

c = Counter(S)
print('No' if bool(c['N']) ^ bool(c['S']) |
      bool(c['W']) ^ bool(c['E']) else 'Yes')
