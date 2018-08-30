import math
from functools import reduce

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

while(True):
    a1,m1,a2,m2,a3,m3 = map(int, input().split())
    if a1 == 0: break
    p = 1
    nx = 0
    while(True):
        nx += 1
        p = a1*p%m1
        if not p-1: break
    p = 1
    ny = 0
    while(True):
        ny += 1
        p = a2*p%m2
        if not p-1: break
    p = 1
    nz = 0
    while(True):
        nz += 1
        p = a3*p%m3
        if not p-1: break
    print(lcm(nx,ny,nz))
