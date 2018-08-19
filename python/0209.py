from sys import stdin
from itertools import product

def rotate_clockwise(matrix):
    return list(map(list, zip(*matrix)))[::-1]

while(True):
    n,m = map(int, stdin.readline().split())
    if not n:
        break
    w = [list(map(int, stdin.readline().split())) for _ in range(n)]
    p = [list(map(int, stdin.readline().split())) for _ in range(m)]
    rp = [p]
    for _ in range(3):
        p = rotate_clockwise(p)
        rp.append(p)
    ds = [[] for _ in range(4)]
    for r,i,j in product(range(4),range(m),range(m)):
        if rp[r][i][j] != -1:
            ds[r].append( [i,j,rp[r][i][j]] )
    for i,j,r in product(range(n-m+1),range(n-m+1),range(4)):
        ans = True
        a = ds[r]
        for k in range(len(a)):
            if w[i+a[k][0]][j+a[k][1]] != a[k][2]:
                ans = False
                break
        if ans:
            print(j+a[0][1]+1,i+a[0][0]+1)
            break
    if not ans: print("NA")
