# C - Palindromic in Both Bases

def ispal(n, base):
    rev, orig = 0, n
    while n:
        rev = rev * base + n % base
        n //= base
    return orig == rev


def gen(limit):
    max_half = 10 ** ((len(str(limit)) + 1) // 2)
    for half in range(1, max_half):
        s = str(half)
        odd = int(s + s[-2::-1])
        even = int(s + s[::-1])
        if odd < limit:
            yield odd
        if even < limit:
            yield even


A, N = int(input()), int(input())
print(sum(n for n in gen(N) if ispal(n, A)))
