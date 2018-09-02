# ref: http://lethe2211.hatenablog.com/entry/2014/12/30/011030
# ref: http://d.hatena.ne.jp/simezi_tan/20101019/1287462266
from heapq import heappop,heappush

if __name__ == '__main__':
    def id(s):
        # edges = [C1 C2 C3...Cm L1 L2 L3...Ln H D]
        # len(edges) = m+n+1+1
        if s[0]=="H": return ne-2
        if s[0]=="D": return ne-1
        num = int(s[1:])
        if s[0]=="C": return num-1
        return num-1+m
    while(True):
        m,n,k,d = map(int, input().split())
        if not m: break
        ne = m+n+2
        cs = list(map(int, input().split()))
        edges = [[] for _ in range(ne) ]
        for i in range(d):
            s1,s2,di = input().split()
            t1,t2,ca = id(s1),id(s2),int(di)*k
            edges[t1].append([t2,ca])
            edges[t2].append([t1,ca])
        que = []
        cost = [float('inf')]*(ne<<m)
        cost[(ne-2)<<m] = 0
        ans = float('inf')
        heappush(que,[0,(ne-2)<<m])
        while(que):
            cc,state = heappop(que)
            vis_cak = state&(2**m-1)
            cur_pos = state>>m
            if cur_pos == ne-1: ans = min(ans,cc)
            if cost[state]>cc: continue
            for ss,dd in edges[cur_pos]:
                nxt_cost = cc+dd
                nxt_pos = ss
                nxt_bit = vis_cak
                # calc cakeshop (visit one time only)
                if 0<=nxt_pos and nxt_pos<m:
                    if 1<<nxt_pos & vis_cak: continue
                    nxt_cost -= cs[nxt_pos]
                    nxt_bit ^= 1 << nxt_pos
                # combine next_position and visited_cakeshop
                new_state = (nxt_pos<<m) + nxt_bit
                if cost[new_state] > nxt_cost:
                    heappush(que,[nxt_cost,new_state])
                    cost[new_state] = nxt_cost
        print(ans)
        