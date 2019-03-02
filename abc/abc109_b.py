N = int(input())
W = [input() for i in range(N)]

history = []
judge = True
for w in W:
    if w in history or (history != [] and history[-1][-1] != w[0]):
        judge = False
        break
    history.append(w)
print('Yes' if judge else 'No')
