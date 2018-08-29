di = {"A":1, "B":0, "C":0}
while(True):
    try:
        x,y = input().split(",")
        di[x],di[y] = di[y],di[x]
    except:
        print([x for x in di.keys() if di[x] == 1][0])
        break