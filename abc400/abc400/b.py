# B - Sum of Geometric Series
N, M = map(int, input().split())
X = sum([N**i for i in range(M + 1)])
print("inf" if X > 10**9 else X)
