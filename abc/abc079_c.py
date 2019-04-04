N = list(map(int, list(input())))

def calc(n1, op, n2):
    if op == '+':
        return n1 + n2
    else:
        return n1 - n2

ops = ['+', '-']

for op1 in ops:
    for op2 in ops:
        for op3 in ops:
            if calc(calc(calc(N[0], op1, N[1]), op2, N[2]), op3, N[3]) == 7:
                break
        else:
            continue
        break
    else:
        continue
    break
print('{}{}{}{}{}{}{}=7'.format(N[0], op1, N[1], op2, N[2], op3, N[3]))
