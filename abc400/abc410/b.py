# B - Reverse Proxy
N, Q = map(int, input().split())
X = list(map(int, input().split()))
B = list([0 for _ in range(N)])
ans = []
for x in X:
    if x == 0:
        i = B.index(min(B))
        B[i] += 1
        ans.append(i+1)
    else:
        B[x-1] += 1
        ans.append(x)
print(*ans)
