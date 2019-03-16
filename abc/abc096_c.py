H, W = map(int, input().split())
s = [list(input()) for i in range(H)]

def judge():
    for i in range(H):
        for j in range(W):
            if s[i][j] == '.':
                continue
            periphery = []
            if i != 0:
                periphery.append(s[i - 1][j])
            if i != H - 1:
                periphery.append(s[i + 1][j])
            if j != 0:
                periphery.append(s[i][j - 1])
            if j != W - 1:
                periphery.append(s[i][j + 1])
            if '#' not in periphery:
                return False
    return True

print('Yes' if judge() else 'No')
