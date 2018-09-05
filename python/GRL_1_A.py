from heapq import heappush,heappop
V,E,r = map(int,input().split())
edges = [[] for _ in range(V)]
for _ in range(E):
    s,t,d = map(int,input().split())
    edges[s].append((t,d))
que = []
mindists = [float("inf")]*V
mindists[r] = 0
heappush(que,(0,r))
while que:
    ccost,cnode = heappop(que)
    if mindists[cnode] < ccost: continue
    for nnode,ncost in edges[cnode]:
        tcost = ccost+ncost
        if mindists[nnode] > tcost:
            mindists[nnode] = tcost
            heappush(que,(tcost,nnode))
print("\n".join(str(e) if e != float("inf") else "INF" for e in mindists))