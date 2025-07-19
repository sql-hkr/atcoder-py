# A - Streamer Takahashi
N, L, R = map(int, input().split())
print(sum(X <= L and R <= Y for X, Y in [map(int, input().split()) for _ in range(N)]))
