Q, L = map(int, input().split())
queries = [input().split() for i in range(Q)]

l = 0
S = []
safe = True
for query in queries:
    if query[0] == 'Push':
        n, m = int(query[1]), int(query[2])
        if l > L - n:
            print('FULL')
            safe = False
            break
        S.append([m, n])
        l += n
    elif query[0] == 'Pop':
        n = int(query[1])
        if l < n:
            print('EMPTY')
            safe = False
            break
        l -= n
        while n > 0:
            if S[-1][1] <= n:
                n -= S[-1][1]
                S.pop()
            else:
                S[-1][1] -= n
                n = 0
    elif query[0] == 'Top':
        if l == 0:
            print('EMPTY')
            safe = False
            break
        print(S[-1][0])
    else:
        print(l)

if safe:
    print('SAFE')
