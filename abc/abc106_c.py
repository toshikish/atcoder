S = input()
K = int(input())

for i in range(len(S)):
    if S[i] != '1':
        break
print('1' if K <= i else S[i])
