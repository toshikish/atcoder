s = input()

ans = False
found_c = False
for l in s:
    if found_c:
        if l == 'F':
            ans = True
            break
    else:
        if l == 'C':
            found_c = True
print('Yes' if ans else 'No')
