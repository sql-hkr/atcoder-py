# B - Four Hidden
T = list(input())
U = input()
idx = [i for i in range(len(T)) if T[i] == "?"]
alp = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(alp)):
    for j in range(len(alp)):
        for k in range(len(alp)):
            for l in range(len(alp)):
                n = [i,j,k,l]
                for m in range(4):
                    T[idx[m]] = alp[n[m]]
                if U in "".join(T):
                    print("Yes")
                    exit()
print("No")
