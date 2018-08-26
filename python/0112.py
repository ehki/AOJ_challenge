from sys import stdin
from itertools import accumulate

while(True):
    n = int(stdin.readline())
    if not n: break
    a = sorted([int(stdin.readline()) for _ in range(n)])
    b = list(accumulate(a))
    print(sum(b[:-1]))
