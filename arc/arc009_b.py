b = list(map(int, input().split()))
tb = {v: i for i, v in enumerate(b)}
N = int(input())
P = []
for i in range(N):
    ai = input()
    converted_ai = ''.join(list(map(lambda x: str(tb[int(x)]), list(ai))))
    P.append((int(converted_ai), int(ai)))

P.sort()
for i in range(N):
    print(P[i][1])
