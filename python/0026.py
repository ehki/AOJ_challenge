ar = [[0]*14 for _ in range(14)]

while(True):
    try:
        x,y,s = map(int,input().split(","))
        if s == 3:
            for x1,y1 in [[-2,0],[0,2],[2,0],[0,-2],[-1,-1],[0,-1],[1,-1],[-1,0],[0,0],[1,0],[-1,1],[0,1],[1,1]]:
                ar[y1+y+2][x1+x+2] += 1
        elif s == 2:
            for x1,y1 in [[-1,-1],[0,-1],[1,-1],[-1,0],[0,0],[1,0],[-1,1],[0,1],[1,1]]:
                ar[y1+y+2][x1+x+2] += 1
        elif s == 1:
            for x1,y1 in [[0,-1],[-1,0],[0,0],[1,0],[0,1]]:
                ar[y1+y+2][x1+x+2] += 1
    except:
        break
br = [ a[2:12] for a in ar[2:12] ]
print(sum([b.count(0) for b in br]))
print(max([max(b) for b in br]))