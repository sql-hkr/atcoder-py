# A - G1
N, A, K = int(input()), list(map(int, input().split())), int(input())
print(sum(1 for i in range(N) if A[i] >= K))
