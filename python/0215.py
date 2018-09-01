while(True):
    W, H = map(int,input().split())
    if not W: break
    ma = [[-1]*(W+2) for _ in range(H+2)]
    for i in range(1,H+1):
        for j,a in enumerate(input()):
            ma[i][j+1] = a
    print(ma)