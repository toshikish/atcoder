from collections import defaultdict

N = int(input())
B = [int(input()) for i in range(N - 1)]

subordinates = defaultdict(list)
for i in range(N, 1, -1):
    if subordinates[i] == []:
        salary = 1
    else:
        salary = max(subordinates[i]) + min(subordinates[i]) + 1
    subordinates[B[i - 2]].append(salary)
print(max(subordinates[1]) + min(subordinates[1]) + 1)
