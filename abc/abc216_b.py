N = int(input())
names = [input() for _ in range(N)]

names.sort()
print('No' if all(names[i] != names[i + 1] for i in range(N - 1)) else 'Yes')
