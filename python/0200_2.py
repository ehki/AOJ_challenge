from decimal import Decimal

class Node:
    def __init__(self, label):
        self.label = label

class Edge:
    def __init__(self, to_node, length):
        self.to_node = to_node
        self.length = length


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, length):
        edge = Edge(to_node, length)
        if from_node.label in self.edges:
            from_node_edges = self.edges[from_node.label]
        else:
            self.edges[from_node.label] = dict()
            from_node_edges = self.edges[from_node.label]
        from_node_edges[to_node.label] = edge


def min_dist(q, dist):
    """
    Returns the node with the smallest distance in q.
    Implemented to keep the main algorithm clean.
    """
    min_node = None
    for node in q:
        if min_node == None:
            min_node = node
        elif dist[node] < dist[min_node]:
            min_node = node

    return min_node

INFINITY = Decimal('Infinity')

def dijkstra(graph, source):
    q = set()
    dist = {}
    prev = {}

    for v in graph.nodes:       # initialization
        dist[v] = INFINITY      # unknown distance from source to v
        prev[v] = INFINITY      # previous node in optimal path from source
        q.add(v)                # all nodes initially in q (unvisited nodes)

    # distance from source to source
    dist[source] = 0

    while q:
        # node with the least distance selected first
        u = min_dist(q, dist)

        q.remove(u)

        if u.label in graph.edges:
            for _, v in graph.edges[u.label].items():
                alt = dist[u] + v.length
                if alt < dist[v.to_node]:
                    # a shorter path to v has been found
                    dist[v.to_node] = alt
                    prev[v.to_node] = u

    return dist, prev


def to_array(prev, from_node):
    """Creates an ordered list of labels as a route."""
    previous_node = prev[from_node]
    route = [from_node.label]
    while previous_node != INFINITY:
        route.append(previous_node.label)
        temp = previous_node
        previous_node = prev[temp]

    route.reverse()
    print(route)
    return route

while(True):
    n,m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graphc = Graph()
    grapht = Graph()
    nodes = []
    for i in range(m):
        node = Node(i)
        nodes.append(node)
        graphc.add_node(node)
        grapht.add_node(node)
    for _ in range(n):
        a,b,c,t = map(int, input().split())
        graphc.add_edge(nodes[a-1],nodes[b-1],c)
        graphc.add_edge(nodes[b-1],nodes[a-1],c)
        grapht.add_edge(nodes[a-1],nodes[b-1],t)
        grapht.add_edge(nodes[b-1],nodes[a-1],t)

    k = int(input())
    for _ in range(k):
        p,q,r = map(int, input().split())
        if r:
            dist, prev = dijkstra(graphc, nodes[p-1])
            print(dist[nodes[q-1]])
        else:
            dist, prev = dijkstra(grapht, nodes[p-1])
            print(dist[nodes[q-1]])
