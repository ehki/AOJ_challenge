from random import randrange
for i in range(30):
    H,W = randrange(5,300),randrange(5,300)
    strs = [[".........................12345"[randrange(30)] for k in range(W)] for j in range(H)]
    strs[randrange(H)][randrange(W)] = "S"
    strs[randrange(H)][randrange(W)] = "G"
    print(W,H)
    for s in strs:
        print("".join(s))
print(0,0)
