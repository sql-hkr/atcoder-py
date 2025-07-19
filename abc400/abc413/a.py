# A - Content Too Large
N, M = map(int, input().split())
if sum(map(int, input().split())) <= M:
    print("Yes")
else:
    print("No")
