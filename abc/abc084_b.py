A, B = map(int, input().split())
S = input()

if S[A] == '-' and S[:A].isdecimal() and S[A + 1:].isdecimal():
    print('Yes')
else:
    print('No')
