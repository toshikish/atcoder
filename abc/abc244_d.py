S = input().replace(' ', '')
T = input().replace(' ', '')

P = ['RGB', 'BRG', 'GBR']
print('Yes' if S in P and T in P or S not in P and T not in P else 'No')
