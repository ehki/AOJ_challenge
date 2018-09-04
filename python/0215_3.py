from itertools import product
from heapq import heappop,heappush
# from array import array
# from math import fabs
from line_profiler import LineProfiler
# def Dijkstra(graph, start, goal):
#     que = [(0, start)]
#     visited = [False] * len(graph)
#     while True:
#         path_len, v = heappop(que)
#         visited[v] = True
#         if v == goal:
#             print(path_len)
#             break
#         for w, edge_len in graph[v].items():
#             if not visited[w]:
#                 heappush(que, (path_len + edge_len, w))

def main():
    while(True):
        W, H = map(int,input().split())
        if not W: break
        # ma = [[-1]*(W+2) for _ in range(H+2)]
        # ps = [[] for _ in range(5)]
        # ma = []
        # ans = float('inf')
        B = float('inf')
        Bi = "NA"
        edges = []
        nodes = [[] for _ in range(5)]
        idx = 0
        for i in range(H):
            for j,a in enumerate(input()):
                if a == "S": edges.append([i,j,idx,5]); ssedge = [i,j,idx,5]; idx+=1
                elif a == "G": edges.append([i,j,idx,6]); ggedge = [i,j,idx,6]; idx+=1
                elif a != ".": edges.append([i,j,idx,int(a)-1]); nodes[int(a)-1].append([i,j,idx,int(a)-1]); idx+=1
        for z in range(5):
            print(z)
            edges[ssedge[2]][3] = z
            dist = [[float('inf')]*idx for _ in range(6)]
            visited = [False] * idx
            dist[1][ssedge[2]] = 0
            que = [(0,1,ssedge[2])]
            while que:
                ccc,num,idd = heappop(que)
                visited[idd] = True
                # print("",end="")
                if idd == ggedge[3]: continue
                if num == 5:
                    if not visited[ggedge[2]]:
                        cost = dist[num][idd] + abs(ggedge[0]-edges[idd][0]) + abs(ggedge[1]-edges[idd][1])
                        if cost < dist[5][ggedge[2]] and cost <B:
                            dist[5][ggedge[2]] = cost
                            heappush(que,(cost,5,ggedge[2]))
                    continue
                nxt = (edges[idd][3]+1)%5
                for n in nodes[nxt]:
                    if not visited[n[2]]:
                        cost = dist[num][idd] + abs(n[0]-edges[idd][0]) + abs(n[1]-edges[idd][1])
                        if cost < dist[num+1][n[2]] and cost < B:
                            dist[num+1][n[2]] = cost
                            heappush(que,(cost,num+1,n[2]))
            if dist[5][ggedge[2]] < B:
                B = dist[5][ggedge[2]]
                Bi = z+1
        print(Bi,B)
        # break
        # print(edges)
        # print(nodes)
        # break
        # abss = [[[ abs(y1-y2)+abs(x1-x2) for y1,x1 in ps[(i+1)%5]] for y2,x2 in ps[i]] for i in range(5) ]
        # starttonext = [ [abs(ss[1]-y2)+abs(ss[0]-x2) for y2,x2 in ps[(i+1)%5]] for i in range(5) ]
        # nexttogoal = [ [abs(gg[1]-y2)+abs(gg[0]-x2) for y2,x2 in ps[(i-1)%5]] for i in range(5) ]
        # test = [[starttonext[0]],[abss[(i+1)%5] for i in range(3)],[nexttogoal[0]]]
        # print(starttonext)
        # print(nexttogoal)
        # print(test)
        # break
if __name__ == "__main__":
    prf = LineProfiler()
    prf.add_function(main)
    prf.runcall(main)
    prf.print_stats()
    # main()