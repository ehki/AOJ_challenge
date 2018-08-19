from sys import stdin
from itertools import product,permutations,combinations

while(True):
    n,s = map(int, stdin.readline().split())
    if not n:
        break
    print(sum([1 for m in combinations(list(range(10)),r=n) if sum(m)==s]))