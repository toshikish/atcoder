N = int(input())
S = input()

T = 'b'
i = 0
len_T = 1
while len_T < N:
    i += 1
    r = i % 3
    if r == 1:
        T = 'a' + T + 'c'
    elif r == 2:
        T = 'c' + T + 'a'
    else:
        T = 'b' + T + 'b'
    len_T += 2
if len_T != N or S != T:
    print(-1)
else:
    print(i)
