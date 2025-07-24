# B - cat 2
N = int(input())
S = [input() for i in range(N)]
print(len(set(s+t for s in S for t in S if s!=t)))
