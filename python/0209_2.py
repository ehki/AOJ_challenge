from random import randrange,random
def rotate_clockwise(matrix):
    return list(map(list, zip(*matrix)))[::-1]

with open("in0209_2.txt", "w") as f:
    for _ in range(3):
        n = randrange(5,10)
        m = randrange(1,n)
        f.write("%d %d\n"%(n,m))
        w = [[ randrange(0,16) if random() > 0.3 else -1 for _ in range(n)] for __ in range(n)]
        psx = randrange(n-m)
        psy = randrange(n-m)
        print(psx+1,psy+1)
        p = [ w[k][psx:psx+m] for k in range(psy,psy+m) ]
        for i in range(randrange(4)):
            p = rotate_clockwise(p)
        for b in w:
            f.write(" ".join(str(e) for e in b))
            f.write("\n")
        for b in p:
            f.write(" ".join(str(e) for e in b))
            f.write("\n")
    f.write("0 0\n")