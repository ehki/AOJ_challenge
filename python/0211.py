from fractions import gcd
from functools import reduce
from sys import stdin

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

while(True):
    n = int(stdin.readline())
    if not n: break
    s = [list(map(int,stdin.readline().split())) for _ in range(n)]
    lcmde = lcm_list([r[1] for r in s])
    lcmnu = lcm_list([r[0]*lcmde//r[1] for r in s])
    print("\n".join( str(lcmnu*r[1]//lcmde//r[0]) for r in s))
