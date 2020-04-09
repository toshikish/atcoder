N, A, B = map(int, input().split())
S = input()

nd = ni = 0
for s in S:
    if s == 'a':
        if nd + ni < A + B:
            nd += 1
            ans = True
        else:
            ans = False
    elif s == 'b':
        if nd + ni < A + B and ni < B:
            ni += 1
            ans = True
        else:
            ans = False
    else:
        ans = False
    print('Yes' if ans else 'No')
