import graph
import sys

def prim_mst(graph):
    visited = set()
    Tree = []
    visited.add('A')
    while len(visited) < len(graph._graph):
        min = sys.maxsize
        min_edge = None
        for s in visited:
            for v in graph._graph[s]:
                if v[0] not in visited:
                    if v[1] < min:
                        min = v[1]
                        min_edge = v
        if min_edge:
            visited.add(min_edge[0])
            Tree.append(min_edge)
            print("Visited => {}".format(visited))
            print("Tree => {}".format(Tree))
        else:
            print("Something went wrong!")
            return


def test():
    g = graph.createTestGraph()
    print(g)
    prim_mst(g)
