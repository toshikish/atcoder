A, B, C, D = map(int, input().split())
print('Yes' if (C + B - 1) // B <= (A + D - 1) // D else 'No')
