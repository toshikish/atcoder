s = input()
k = int(input())

if len(s) < k:
    ans = 0
else:
    bag = set()
    for i in range(len(s) - k + 1):
        bag.add(s[i:i+k])
    ans = len(bag)
print(ans)
