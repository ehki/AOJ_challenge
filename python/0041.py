from sys import stdin
from itertools import permutations,product

while(True):
    lis = stdin.readline().split()
    if lis == ["0","0","0","0"]: break
    for [a,b,c,d],[e,f,g],h in product(permutations(lis),product(["+","*","-"],repeat=3),range(7)):
        st = "("*(h>>2)+a+e+\
                "("*(1 if h in [2,3] else 0)+b+\
                ")"*(1 if h in [4,5] else 0)+f+\
                "("*(1 if h in [1,5] else 0)+c+\
                ")"*(1 if h in [2,6] else 0) +g+d+\
                ")"*(h&5>>2)
        if eval(st) == 10: print(st); break
    else:
        print(0)
