S = input()
Q = int(input())
queries = [input().split() for i in range(Q)]

head = []
tail = []
forward = True
for query in queries:
    if query[0] == '1':
        forward = not forward
    else:
        if query[1] == '1' and forward or query[1] == '2' and not forward:
            head.append(query[2])
        else:
            tail.append(query[2])

if forward:
    ans = ''.join(head[::-1]) + S + ''.join(tail)
else:
    ans = ''.join(tail[::-1]) + S[::-1] + ''.join(head)
print(ans)
