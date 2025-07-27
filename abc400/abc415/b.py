# B - Pick Two
S = input()
c = False
for i in range(len(S)):
    if S[i] == "#":
        if c:
            print(i + 1)
            c = False
        else:
            print(f"{i + 1},", end="")
            c = True
