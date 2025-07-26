# B - Citation
N = int(input())
A = list(map(int, input().split()))
S = sorted(list(set(A)), reverse=True)
c = 0
for s in S:
    c += A.count(s)
    if c >= s:
        print(s)
        exit()
