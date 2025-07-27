# C - Mixture
T = int(input())
for _ in range(T):
    N = int(input())
    S = "0" + input()
    ok = [False for _ in range(1 << N)]
    ok[0] = True
    for i in range(1 << N):
        if not ok[i]:
            continue
        for j in range(N):
            if i & (1 << j):
                continue
            next = i | (1 << j)
            if S[next] == "0":
                ok[next] = True
    if ok[(1 << N) - 1]:
        print("Yes")
    else:
        print("No")
