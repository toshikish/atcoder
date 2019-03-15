s = input()
K = int(input())

N = len(s)
words = set()
for k in range(K):
    for i in range(N - k):
        words.add(s[i:i + k + 1])
print(sorted(words)[K - 1])
