s = input()
print(min(max(len(p) for p in s.split(l)) for l in set(list(s))))
