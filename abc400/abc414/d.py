# D - Transmission Mission
N, M = map(int, input().split())
X = sorted(list(map(int, input().split())))
d = sorted([X[i + 1] - X[i] for i in range(N - 1)])
print(sum(d[i] for i in range(N - M)))
