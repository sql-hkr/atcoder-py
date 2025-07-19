# A - Conflict
N, T, A = int(input()), input(), input()
print("Yes" if sum(t == a == "o" for t, a in zip(T, A)) else "No")
