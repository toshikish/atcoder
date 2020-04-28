S = input()

if S == '{}':
    is_dict = True
else:
    is_dict = False
    level = 1
    for i in range(1, len(S)):
        if S[i] == '{':
            level += 1
        elif S[i] == '}':
            level -= 1
        elif S[i] == ':' and level == 1:
            is_dict = True
            break
print('dict' if is_dict else 'set')
