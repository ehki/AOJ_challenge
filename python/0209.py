from sys import stdin
from itertools import product
# from line_profiler import LineProfiler

def rotate_clockwise(matrix):
    return list(map(list, zip(*matrix)))[::-1]

def main():
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
        ds = [[ [i,j,rp[r][i][j]] for i,j in product(range(m),range(m)) if rp[r][i][j] != -1] for r in range(4)]
        flag = True
        for i,j,a in product(range(n-m+1),range(n-m+1),ds):
            for b in a:
                if w[i+b[0]][j+b[1]] - b[2]:
                    break
            else:
                print(j+a[0][1]+1,i+a[0][0]+1)
                flag = False
                break
        if flag: print("NA")

if __name__ == "__main__":
    # prf = LineProfiler()
    # prf.add_function(main)
    # prf.runcall(main)
    # prf.print_stats()
    main()