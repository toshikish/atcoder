N = int(input())

def dfs(s):
    if int(s) > N:
        return 0
    ans = 1 if all(s.count(c) > 0 for c in '753') else 0
    for c in '753':
        ans += dfs(s + c)
    return ans

print(dfs('0'))
