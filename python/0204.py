while(True):
    ans = 0
    R, N = map(int, input().split())
    R = float(R)
    if R == 0 and N == 0:
        break
    d = []
    for _ in range(N):
        d.append(list(map(float, input().split())))
    for i in range(len(d)-1,-1,-1):
        x,y = d[i][0],d[i][1]
        d[i][0] = (x**2+y**2)**0.5
        d[i].append(x/d[i][0])
        d[i].append(y/d[i][0])
        if d[i][0] <= R:
            ans += 1
            del d[i]
    while(True):
        if not len(d): print(ans); break
        for i in range(len(d)-1,-1,-1):
            d[i][0] -= d[i][3]
            if d[i][0] <= R:
                ans += 1
                del d[i]
        if not len(d): print(ans); break
        d.sort(key=lambda x: x[0])
        for j in range(len(d)-1,0,-1):
            X = d[j][0]*d[j][4]
            Y = d[j][0]*d[j][5]
            if (d[j][4]*d[0][4]+d[j][5]*d[0][5] ) < 0:
                xv = R*d[0][4]
                yv = R*d[0][5]
                if ((X-xv)**2+(Y-yv)**2)**0.5 < d[j][2]:
                    del d[j]
                continue
            if ( abs((d[0][5]*X-d[0][4]*Y)) < d[j][2] ):
                del d[j]
        del d[0]

