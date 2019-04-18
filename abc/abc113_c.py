from collections import defaultdict

N, M = map(int, input().split())
years = defaultdict(list)
Q = []
for i in range(M):
    P, Y = map(int, input().split())
    years[P].append(Y)
    Q.append((P, Y))

rev_list = {}
for P, Y in years.items():
    Y.sort()
    rev_list[P] = {}
    for i in range(len(Y)):
        rev_list[P][Y[i]] = i + 1

for q in Q:
    print('{:06}{:06}'.format(q[0], rev_list[q[0]][q[1]]))
