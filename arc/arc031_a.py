name = input()

cyclic = True
N = len(name)
for i in range(N // 2):
    if name[i] != name[N - i - 1]:
        cyclic = False
        break
print('YES' if cyclic else 'NO')
