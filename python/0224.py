# ref: http://lethe2211.hatenablog.com/entry/2014/12/30/011030
# ref: http://d.hatena.ne.jp/simezi_tan/20101019/1287462266
from heapq import heappop,heappush

if __name__ == '__main__':
    def id(s):
        if s[0]=="H": return ne-2
        if s[0]=="D": return ne-1
        num = int(s[1:])
        if s[0]=="C": return num-1
        return num-1+m
    while(True):
        m,n,k,d = map(int, input().split())
        if not m: break
        ne = m+n+2
        node = ne*(1<<m)
        cs = list(map(int, input().split()))
        edges = [[] for _ in range(node) ]
        for i in range(d):
            s1,s2,di = input().split()
            t1,t2,ca = id(s1),id(s2),int(di)*k
            edges[t1].append([t2,ca])
            edges[t2].append([t1,ca])
        que = []
        d = [float('inf')]*7000
        d[(ne-2)*(1<<m)] = 0
        ans = float('inf')
        heappush(que,[0,(ne-2)*(1<<m)])
        while(que):
            cc,cnode = heappop(que)
            bit, cur = cnode%(1<<m), cnode//(1<<m)
            if cur == ne-1: ans = min(ans,cc)
            if d[cnode]>cc: continue
            for ss,dd in edges[cur]:
                nc = cc+dd
                nxt = ss
                nbit = bit
                if 0<=nxt and nxt<m:
                    if 1<<nxt & bit: continue
                    nc -= cs[nxt]
                    nbit ^= 1<< nxt
                nxt = nxt*(1<<m)+nbit
                if d[nxt]>nc: heappush(que,[nc,nxt]); d[nxt]=nc
        print(ans)
        