# B - Ranking with Ties
N = int(input())
P = list(map(int, input().split()))
for i in range(N):
    r = 1
    for j in range(N):
        if P[j] > P[i]:
            r += 1
    print(r)
