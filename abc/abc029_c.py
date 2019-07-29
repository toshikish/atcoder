N = int(input())

l = ['a', 'b', 'c']
for i in range(3 ** N):
    p = ''
    for j in range(N):
        p = l[i % 3] + p
        i //= 3
    print(p)
