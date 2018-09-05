from itertools import product
V,E = map(int,input().split())
edges = [tuple() for _ in range(E)]
dist = [[float("inf")]*V for _ in range(V)]
for i in range(V):
    dist[i][i] = 0
for _ in range(E):
    s,t,d = map(int,input().split())
    dist[s][t] = d
for k,i,j in product(range(V),range(V),range(V)):
    if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
        dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
for i in range(V):
    if dist[i][i] < 0:
        print("NEGATIVE CYCLE")
        exit()
for i in range(V):
    ans = ["INF" if dist[i][j] == float("inf") else dist[i][j] for j in range(V)]
    print(" ".join(map(str, ans)))
