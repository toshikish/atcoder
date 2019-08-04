N = int(input())

if N <= 9:
    ans = N
elif N <= 99:
    ans = 9
elif N <= 999:
    ans = 9 + N - 100 + 1
elif N <= 9999:
    ans = 9 + 900
elif N <= 99999:
    ans = 9 + 900 + N - 10000 + 1
else:
    ans = 9 + 900 + 90000
print(ans)
