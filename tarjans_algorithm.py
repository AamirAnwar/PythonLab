import graph

Time = 0
Time = 0

def _tarjan_util(v,low,disc,stack_set,st, graph, parent):
    global Time
    disc[v] = Time
    low[v] = Time
    Time += 1
    stack_set.add(v)
    st.append(v)

    for vertex in graph[v]:
        if disc[vertex[0]] == -1:
            parent[vertex[0]] = v
            _tarjan_util(vertex[0], low, disc, stack_set, st, graph,parent)
            low[v] = min(low[v], low[vertex[0]])
        elif vertex[0] in stack_set:
            if parent[v] != vertex[0]:
                low[v] = min(low[v], disc[vertex[0]])

    w = ''
    if low[v] == disc[v]:
        print("Found an SCC!")
        while w != v:
            w = st.pop()
            print(w, end="")
            stack_set.remove(w)
        print("\r")

def tarjan(graph):
    n = len(graph)
    result = set()
    disc = dict()
    low = {}
    vertices = ['D','A', 'B', 'C','E','F','G','H']
    parent = {}
    for v in vertices:
        disc[v] = -1
        low[v] = -1
        parent[v] = v
    stack_set = set()
    st = []


    for v in vertices:
        if disc[v] == -1:
            _tarjan_util(v, low, disc, stack_set, st, graph,parent)
    print("Discovery times are {}".format(disc))
    print("Low times are {}".format(low))
    print("Parents are {}".format(parent))

    for v in graph:
        for vertex in graph[v]:
            # print("Looking at {} => {}".format(v,vertex))
            if  disc[v] <= low[vertex[0]]:
                result.add(v)
                # print("Found an articulation point! {}".format(v))
    print("Articulation points are => {}".format(result))

def test():
    connections = [('A','C',1), ('A','B',1), ('B','C',1), ('D','C',1), ('D','E',1),('E','G',1),('E','F',1),('F','G',1),('F','H',1)]
    g = graph.Graph(False)
    g.addConnections(connections)
    tarjan(g._graph)
