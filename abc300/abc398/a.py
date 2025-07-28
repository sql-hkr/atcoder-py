# A - Doors in the Center
N = int(input())
if N % 2:
    c = (N - 1) // 2
    print("-" * c + "=" + "-" * c)
else:
    c = (N - 2) // 2
    print("-" * c + "=" * 2 + "-" * c)
