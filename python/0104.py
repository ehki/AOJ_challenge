
while(True):
    ny,nx = map(int, input().split())
    if nx == 0 and ny == 0:
        break
    dic = {">":[1,0],"<":[-1,0],"^":[0,-1],"v":[0,1],".":[0,0]}
    poshist = []
    ma = [input() for i in range(ny)]
    px,py = 0,0
    poshist.append([px,py])
    while(True):
        px += dic[ma[py][px]][0]
        py += dic[ma[py][px]][1]
        if [px,py] in poshist:
            poshist.append([px,py])
            break
        else:
            poshist.append([px,py])
    if poshist[-1] == poshist[-2]:
        print(poshist[-1][0],poshist[-1][1])
    else:
        print('LOOP')