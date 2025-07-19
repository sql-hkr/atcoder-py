# B - String Too Long
N = int(input())
cl = [list(map(str, input().split())) for _ in range(N)]
if sum(map(lambda x: int(x[1]), cl)) > 100:
    print("Too Long")
else:
    print("".join(map(lambda x: x[0]*int(x[1]), cl)))
