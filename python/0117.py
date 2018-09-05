from heapq import heappop, heappush
def solve(graph,start,goal,numnodes):
    que = []
    heappush(que,(0,start-1))
    mindists = [float("inf")]*numnodes
    while que:
        ccost,cnode = heappop(que)
        if mindists[cnode] < ccost: continue
        for nnode,mcost in graph[cnode]:
            tcost = ccost+mcost
            if mindists[nnode] > tcost:
                mindists[nnode] = tcost
                heappush(que,(tcost,nnode))
    return mindists[goal-1]
n = int(input())
m = int(input())
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b,c,d = map(int,input().split(","))
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,d))
s,g,V,P = map(int, input().split(","))
V -= solve(graph,s,g,n)
V -= P
V -= solve(graph,g,s,n)
print(V)