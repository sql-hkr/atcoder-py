# B - Precondition
S = input()
T = input()
for i in range(len(S)):
    if i==0:
        continue
    if S[i].isupper() and S[i-1] not in T:
        print("No")
        exit()
print("Yes")
