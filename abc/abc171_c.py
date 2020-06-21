N = int(input())

ans = []
while N >= 1:
    N -= 1
    ans.append(chr(97 + N % 26))
    N //= 26
print(''.join(ans[::-1]))
