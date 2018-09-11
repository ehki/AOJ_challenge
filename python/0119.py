m = int(input())
n = int(input())
edges = [[] for _ in range(m)]
for _ in range(n):
    x,y = map(int,input().split())
    edges[x-1].append(y-1)
L = []
visited = [False]*m
def visit(node):
    if not visited[node]:
        visited[node] = True
        for nn in edges[node]:
            visit(nn)
        L.append(node)
for node in range(m):
    visit(node)
for e in L[::-1]:
    print(e+1)