from random import randrange

with open("in0210_2.txt","w") as f:
    for _ in range(20):
        W,H = randrange(1,31),randrange(1,31)
        f.writelines("%d %d\n"%(W,H))
        arr = ["".join("....##ENWSX"[randrange(11)] for _ in range(W)) for _ in range(H)]
        arr[0] = "".join("##X"[randrange(3)] for _ in range(W))
        arr[-1] = "".join("##X"[randrange(3)] for _ in range(W))
        for i in range(1,H-1):
            arr[i] = "##X"[randrange(3)] + arr[i][1:-1] + "##X"[randrange(3)]
        for n in arr:
            f.writelines(n+"\n")
    f.writelines("%d %d\n"%(0,0))