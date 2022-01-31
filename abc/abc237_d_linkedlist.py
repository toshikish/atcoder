from re import I


N = int(input())
S = input()

left = [-1] * (N + 1)
left[0] = 'S'
s = 0
right = [-1] * (N + 1)
right[0] = 'E'
e = 0

for i in range(N):
    if S[i] == 'L':
        left[i + 1] = left[i]
        if left[i] == 'S':
            s = i + 1
        else:
            right[left[i]] = i + 1
        left[i] = i + 1
        right[i + 1] = i
    else:
        right[i + 1] = right[i]
        if right[i] == 'E':
            e = i + 1
        else:
            left[right[i]] = i + 1
        right[i] = i + 1
        left[i + 1] = i

ans = [s]
i = s
for _ in range(N):
    i = right[i]
    ans.append(i)
print(' '.join(list(map(str, ans))))
