# B - Bingo
A = [] 
M = [[False for _ in range(3)] for _ in range(3)]
for _ in range(3):
    A.append(list(map(int, input().split())))

N = int(input())
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                M[i][j] = True

bingo = False

for i in range(3):
    if M[i][0] + M[i][1] + M[i][2]:
        bingo = True
    if M[0][i] + M[1][i] + M[2][i]:
        bingo = True

if M[0][0] + M[1][1] + M[2][2]:
    bingo = True

if M[2][0] + M[1][1] + M[0][2]:
    bingo = True

if bingo:
    print("Yes")
else:
    print("No")

