S = input()

T = {'O': 0, 'D': 0, 'I': 1, 'Z': 2, 'S': 5, 'B': 8}
for i in range(10):
    T[str(i)] = i
print(''.join(list(map(lambda s: str(T[s]), S))))
