# A - Task Failed Successfully
N = int(input())
ans = 0
for i in range(N):
    A, B = map(int, input().split())
    if B - A > 0:
        ans += 1
print(ans)
