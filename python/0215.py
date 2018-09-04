from itertools import product
# from array import array
# from math import fabs
# from line_profiler import LineProfiler
def main():
    while(True):
        W, H = map(int,input().split())
        if not W: break
        # ma = [[-1]*(W+2) for _ in range(H+2)]
        ps = [[] for _ in range(5)]
        ans = float('inf')
        for i in range(H):
            for j,a in enumerate(input()):
                if a == "S": ss = [i,j]
                elif a == "G": gg = [i,j]
                elif a != ".": ps[int(a)-1].append([i,j])
        # if [1 for i in range(5) if len(ps[i])==0]:
        #     print("NA"); continue
        # print(ps)
        B = float('inf')
        Bi = -1
        abss = [[[ abs(y1-y2)+abs(x1-x2) for y1,x1 in ps[(i+1)%5]] for y2,x2 in ps[i]] for i in range(5) ]
        # print(abss)
        # break
        for mon1 in range(5):
            dp = [[float('inf')]*1000 for _ in range(5)]
            # cand = [[0,ss[0][0],ss[0][1]]]
            now = (mon1+1)%5
            dpCacheNow = dp[now]
            emCacheNow = ps[now]
            for i,[ty,tx] in enumerate(emCacheNow):
                dpCacheNow[i] = abs(ss[0]-ty) + abs(ss[1]-tx)
            for e in range(3):
                nxt = (now+1)%5
                dpCacheNxt = dp[nxt]
                emCacheNxt = ps[nxt]
                for [nowy,nowx],[i,dpnow] in zip(emCacheNow,enumerate(dpCacheNow)):
                    abssCacheNow = abss[now][i]
                    # if dpCacheNow[i] > B:
                    #     print("",end="")
                    #     continue
                    dpCacheNxt = [min(dpc,dpnow+abc) for dpc,abc in zip(dpCacheNxt,abssCacheNow)]
                    # for j in range(len(emCacheNxt)):
                        # if abss[now][i][j] > B:
                        #     print("",end="")
                        #     continue
                        # print(now,nxt)
                        # dpCacheNxt[j] = 
                now = nxt
                dpCacheNow = dpCacheNxt
                emCacheNow = emCacheNxt
            for i,[ey,ex] in enumerate(emCacheNxt):
                tmp = dpCacheNxt[i] + abs(gg[0]-ey) + abs(gg[1]-ex)
                if tmp < B:
                    B = tmp
                    Bi = mon1
            # for mon2 in range(5):
            #     # dpCacheNow = dp[mon2]
            #     # dpCacheNxt = dp[(mon1+mon2+1)%5]
            #     # dpCacheNow[0] = 0
            #     nxt = ps[(mon1+mon2+1)%5] if mon2<4 else gg
            #     # print(nxt)
            #     # print(cand)
            #     tmp = []
            #     for i,[ty,tx] in enumerate(nxt):
            #         # if dpCacheNow[i] >= B:
            #         #     continue
            #         tc = float('inf')
            #         # for cc,cy,cx in cand:
            #         for cc,cy,cx in cand:
            #             # if cc > B:
            #             #     # print("a",end="")
            #             #     tc = float('inf')
            #             #     break
            #             # else:
            #             tc = min(tc,abs(ty-cy)+abs(tx-cx)+cc)
            #             tc
            #         tmp.append([tc,ty,tx])
            #         # dpCacheNxt[i] = min(dpCacheNxt[i],tc)
            #     cand = tmp
            # if cand[0][0] < B:
            #     B = cand[0][0]
            #     Bi = mon1
        if(Bi == -1):
            print("NA")
        else:
            print("%d %d"%(Bi+1,B))
        # for mon1 in range(5):
        #     mon2 = (mon1+1)%5
        #     dp = [[float('inf')]*1000 for _ in range(5)]
        #     for i,yx in enumerate(ps[mon2]):
        #         dp[mon2][i] = abs(ss[0]-yx[0])+abs(ss[1]-yx[1])
        #     mon3 = mon2
        #     for mon3 in range(mon2,mon2+3):
        #         mon3 = mon3%5
        #         mon4 = (mon3+1)%5
        #         for [i,yx],[j,nyx] in product(enumerate(ps[mon3]),enumerate(ps[mon4])):
        #             dp[mon4][j] = min(dp[mon4][j],dp[mon3][i]+abs(yx[0]-nyx[0])+abs(yx[1]-nyx[1]))
        #     mon5 = (mon1-1)%5
        #     for i,yx in enumerate(ps[mon5]):
        #         d = dp[mon5][i] + abs(gg[0]-yx[0])+abs(gg[1]-yx[1])
        #         if ans > d:
        #             ans,ansi = d,mon1
        # print(ansi+1,ans)

if __name__ == "__main__":
    # prf = LineProfiler()
    # prf.add_function(main)
    # prf.runcall(main)
    # prf.print_stats()
    main()