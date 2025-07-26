# B - Grid Rotation
N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]
ans = N*N+4
rot90 = lambda S: list(zip(*S[::-1]))
diff = lambda S, T: sum([1 for si, ti in zip(S, T) for sij, tij in zip(si, ti) if sij != tij])
for i in range(4):
    ans = min(ans, diff(S, T)+i)
    S = rot90(S)
print(ans)
