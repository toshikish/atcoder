from collections import Counter

N = int(input())
c = input()

C = Counter(c)
print(max(C.values()), min(C.values()) if len(C) == 4 else 0)
