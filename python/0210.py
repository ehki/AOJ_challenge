from sys import stdin
# from line_profiler import LineProfiler

def main():

    head = [[8,1,2,4],[1,2,4,8],[2,4,8,1],[4,8,1,2]]

    while(True):
        W,H = map(int, stdin.readline().split())
        m = [[0]*W for _ in range(H)]
        ps = []
        if not (W or H): break
        for h in range(H):
            s = stdin.readline()
            for w in range(W):
                if s[w] in [".", "X", "E", "N", "W", "S"]:
                    m[h][max(0,w-1)] |= 1
                    m[min(H-1,h+1)][w] |= 2
                    m[h][min(W-1,w+1)] |= 4
                    m[max(0,h-1)][w] |= 8
                if s[w] in ["E", "N", "W", "S"]:
                    ps.append([h,w,["E", "N", "W", "S"].index(s[w])])
                if s[w] == "X":
                    m[h][w] |= 16
        if W <= 2 or H <= 2:
            print(1)
            continue
        ttt = 0
        while(True):
            ttt += 1
            if ttt > 180: print("NA"); break
            dest = []
            positions = [a[:2] for a in ps]
            for pi,p in enumerate(ps):
                for i in range(4):
                    if head[p[2]][i] & m[p[0]][p[1]]:
                        d = head[p[2]][i]
                        if   d == 1 and not [p[0],p[1]+1] in positions: p[2] = 0; dest.append([pi,2,p[0],p[1]+1]); break
                        elif d == 2 and not [p[0]-1,p[1]] in positions: p[2] = 1; dest.append([pi,3,p[0]-1,p[1]]); break
                        elif d == 4 and not [p[0],p[1]-1] in positions: p[2] = 2; dest.append([pi,0,p[0],p[1]-1]); break
                        elif d == 8 and not [p[0]+1,p[1]] in positions: p[2] = 3; dest.append([pi,1,p[0]+1,p[1]]); break
                else:
                    dest.append([pi,(p[2]+2)&3,p[0],p[1]])
            dest = sorted(dest,key=lambda x: (x[2:],x[1]))
            dellist = []
            for pi,d,dy,dx in dest:
                if not [dy,dx] in positions: positions.append([dy,dx]); ps[pi][:2] = [dy,dx]
                if m[ps[pi][0]][ps[pi][1]] & 16: dellist.append(pi)
            for idx in sorted(dellist)[::-1]: del ps[idx]
            if not len(ps): print(ttt); break

if __name__ == "__main__":
    # prf = LineProfiler()
    # prf.add_function(main)
    # prf.runcall(main)
    # prf.print_stats()
    main()