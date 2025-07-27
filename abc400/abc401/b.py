# B - Unauthorized
N = int(input())
S = [input() for _ in range(N)]
l = False
e = 0
for s in S:
    if s == "login":
        l = True
    elif s == "logout":
        l = False
    elif s == "private" and not l:
        e += 1
print(e)
