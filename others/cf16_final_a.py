H, W = map(int, input().split())
S = [list(input().split()) for i in range(H)]

h = w = 0
for i in range(H):
    if 'snuke' in S[i]:
        h = i
        w = S[i].index('snuke')
        break
print(chr(ord('A') + w) + str(h + 1))
