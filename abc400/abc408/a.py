# A - Timeout
N, S = map(int, input().split())
T = list(map(int, input().split()))
print("No" if T[0] > S or any(T[i] - T[i - 1] > S for i in range(1, N)) else "Yes")
