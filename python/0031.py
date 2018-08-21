from sys import stdin
from itertools import product,permutations,combinations

while(True):
    try:
        n = int(stdin.readline())
        a = str(bin(n))
        print(" ".join(str(2**i) for i,s in enumerate(a[:1:-1]) if s=="1"))
    except:
        break
