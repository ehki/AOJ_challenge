from heapq import heappush, heappop

def Dijkstra(graph, start, goal):
    que = [(0, start)]
    visited = [False] * len(graph)
    while True:
        path_len, v = heappop(que)
        visited[v] = True
        if v == goal:
            print(path_len)
            break
        for w, edge_len in graph[v].items():
            if not visited[w]:
                heappush(que, (path_len + edge_len, w))

while(True):
    dicco = {}
    dicti = {}
    n,m = map(int, input().split())
    if n == 0 and m == 0:
        break
    for i in range(m):
        dicco[i] = {}
        dicti[i] = {}
    for _ in range(n):
        a,b,c,t = map(int, input().split())
        dicco[a-1][b-1] = c
        dicco[b-1][a-1] = c
        dicti[a-1][b-1] = t
        dicti[b-1][a-1] = t
    k = int(input())
    for _ in range(k):
        p,q,r = map(int, input().split())
        if not r:
            Dijkstra(dicco, p-1, q-1)
        else:
            Dijkstra(dicti, p-1, q-1)

