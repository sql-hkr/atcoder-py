S = input()
x = "abcdefghijklmnopqrstuvwxyz"
for s in S:
    x = x.replace(s, "")
print(x[0])
