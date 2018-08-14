while(True):
    X,Y = map(int, input().split())
    if X==0 and Y==0:
        break
    ar = [list(map(int, input().split())) for _ in range(Y)]
    ar.append([0]*X)
    br = [[0]*X for _ in range(Y+1)]
    for j in range(X):
        if ar[-2][j] != 1:
            br[-2][j] = 1
        br[-1][j] = 1
    for i in range(Y-2,-1,-1):
        for j in range(X):
            if j-1 >= 0 and ar[i][j] != 2 and ar[i+1][j-1] == 0: br[i][j] += br[i+1][j-1]
            if j+1 < X and ar[i][j] != 2 and ar[i+1][j+1] == 0: br[i][j] += br[i+1][j+1]
            if ar[i][j] != 2 and ar[i+1][j] != 1: br[i][j] += br[i+1][j]
            if ar[i][j] == 2 and ar[i+2][j] != 1: br[i][j] += br[i+2][j]
        for j in range(X):
            if ar[i][j] == 1: br[i][j] = 0
    print(sum(br[0]))
