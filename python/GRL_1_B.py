V,E,r = map(int,input().split())
edges = [tuple(map(int,input().split())) for _ in range(E)]
dist = [float("inf") for _ in range(V)]
dist[r-1] = 0
for i in range(V+1):
    for edge in edges:
        if edge[0] != float("inf") and dist[edge[1]-1] > dist[edge[0]-1]+edge[2]:
            dist[edge[1]-1] = dist[edge[0]-1]+edge[2]
            if i==V-1: print("NEGATIVE CYCLE"); exit()
print("\n".join(str(dist[e-1]) if dist[e-1] != float("inf") else "INF" for e in range(V)))