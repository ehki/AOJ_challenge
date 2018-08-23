from random import randrange

with open("in0211_2.txt","w") as f:
    for _ in range(10):
        n = randrange(2,11)
        f.writelines("%d\n"%(n))
        for _ in range(n):
            f.writelines("%d %d\n"%(randrange(1,10001),randrange(1,10001)))
    f.writelines("%d\n"%(0))