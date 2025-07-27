# B - Restaurant Queue
from collections import deque

Q = int(input())
q = deque()
for _ in range(Q):
    a, *b = map(int, input().split())
    if a == 1:
        q.append(b[0])
    else:
        print(q.popleft())
