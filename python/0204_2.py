from random import randrange

with open("in0204_2.txt", "w") as f:
    for _ in range(20):
        R = randrange(1,500)
        N = randrange(1,100)
        f.write("%d %d\n"%(R,N))
        for i in range(N):
            x,y,r,v = randrange(-100,1000),randrange(-100,1000),randrange(1,500),randrange(1,500)
            f.write("%d %d %d %d\n"%(x,y,r,v))
    f.write("0 0\n")