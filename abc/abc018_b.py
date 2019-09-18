S = input()
N = int(input())
len_S = len(S)
for i in range(N):
    l, r = map(int, input().split())
    if l - 2 < 0:
        S = S[0:l - 1] + S[r - 1::-1] + S[r:len_S]
    else:
        S = S[0:l - 1] + S[r - 1:l - 2:-1] + S[r:len_S]
print(S)
