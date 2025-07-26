# B - Product Calculator
N, K = map(int, input().split())
A = list(map(int, input().split()))
M = 10**K-1
ans = 1
for a in A:
    ans *= a
    if ans > M:
        ans = 1
print(ans)
