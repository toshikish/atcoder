s = input()

len_s = len(s)
for i in range(len_s):
    if s[i] == 'A':
        start = i
        break
for i in range(len_s - 1, -1, -1):
    if s[i] == 'Z':
        end = i
        break
print(end - start + 1)
