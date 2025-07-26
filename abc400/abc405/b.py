# B - Not All
N, M = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    e = True
    for j in range(1, M + 1):
        if j not in A:
            e = False
    if e:
        A.pop()
    else:
        print(i)
        exit()
