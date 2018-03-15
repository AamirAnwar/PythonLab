import graph
import sys
def bellman_ford_algorithm(g):
    print(dict(g))
    n = len(g)
    dist = {}
    vertices = ['A', 'B', 'C', 'D','E']
    for v in vertices:
        dist[v] = sys.maxsize

    dist['A'] = 0
    print(dist)
    for i in range(0,n - 1):
        print("Path length is {}".format(i))
        for v in g:
            for edge in g[v]:
                if dist[v] != sys.maxsize and dist[v] + edge[1] < dist[edge[0]]:
                    dist[edge[0]] = dist[v] + edge[1]
    print(dist)
    for v in g:
        for edge in g[v]:
            if dist[v] != sys.maxsize and dist[v] + edge[1] < dist[edge[0]]:
                print("Negative cycle found! :(")
                return





def test():
    connections = [('A', 'B', 2), ('C','A',-4) ,('B', 'C', 1), ('B', 'D', 2),
                   ('D', 'E', 2), ('C','E', 4)]
    g = graph.Graph(True)
    g.addConnections(connections)
    bellman_ford_algorithm(g._graph)
