import graph
from collections import defaultdict



def find_parent(parent, vertex):

    if parent[vertex] == vertex:
        return vertex
    else:
        return find_parent(parent, parent[vertex])

def union(parent,rank,x,y):

    xroot = find_parent(parent, x)
    yroot = find_parent(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else :
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal_mst(g):

    # Sort all edges
    result = []
    V = len(g)
    rank = {}
    parent = {}
    edge_list = []
    for i in g:
        edges = g[i]
        for e in edges:
            edge_list.append((i,e[0],e[1]))

    edge_list = sorted(edge_list, key = lambda x:x[2])
    for vertex in g:
        parent[vertex] = vertex
        rank[vertex] = 0
    e = 0
    i = 0
    while e < V-1:
        s,d,w = edge_list[i]
        i += 1
        x = find_parent(parent,s)
        y = find_parent(parent,d)
        if x != y:
            e += 1
            result.append((s,d,w))
            union(parent,rank,x,y)
    print(result)


def test():
    g = graph.createTestGraph()
    kruskal_mst(g._graph)
    # print(g)
