from collections import defaultdict
from queue import Queue
from stack import Stack
from time import sleep


class Graph(object):
    def __init__(self, directed=False):
        self._graph = defaultdict(list)
        self._directed = directed

    def addConnections(self, connections):
        for v1, v2, weight in connections:
            self.add(v1, v2, weight)

    def add(self, v1, v2, weight):
        self._graph[v1].append((v2, weight))
        if self._directed == False:
            self._graph[v2].append((v1, weight))

    def showGraph(self):
        for item in self._graph.items():
            print(item)

    def remove(self, v):
        for n, con in self._graph.items():
            i = 0
            while i < len(con):
                vertex, weight = con[i]
                if vertex == v:
                    con.remove(con[i])
                i += 1
        try:
            del self._graph[v]
        except KeyError:
            print("Key error exception!")
            pass

    def findPath(self, v1, v2, path=[]):
        path = path + [v1]
        if v1 == v2:
            return path

        if not self._graph[v1]:
            return None

        for vertex, weight in self._graph[v1]:
            if vertex not in path:
                newPath = self.findPath(vertex, v2, path)
                if newPath:
                    return newPath
        return None

    def __str__(self):
        '''Helpful in debugging'''
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


    def DFSUtil(self, start, visited):
        visited.add(start)
        for node in self._graph[start]:
            if not node in visited:
                self.DFSUtil(node, visited)
        #print("Finished visited all edges from {}".format(start))


    def performDFS(self):
        '''Perform basic depth first search'''
        keys = self._graph.keys()
        visited = set()
        self.DFSUtil(keys[0],visited)


    def depthFirstSearch(self):
        print("Running depth first search in O(V + E)...")
        sleep(1)
        S = Stack()
        op = []
        S.push('A')
        self._dfs(S,op)

    def _dfs(self, S, op):
        if S.isEmpty():
            return
        current = S.peek()
        for v in self._graph[current]:
            if v[0] not in op and v[0] not in S.list:
                S.push(v[0])
                self._dfs(S,op)
        e = S.pop()
        print(e, end=" => ")
        op.append(e)




    def performBFS(self):
        print("Running Breadth first search in  O(V + E)...")
        sleep(2)
        q = Queue()
        q.enqueue('A')
        op = []
        self._bfs(q,op)

    def _bfs(self, q, op):
        if q.isEmpty():
            return
        e = q.dequeue()
        print(e, end=" => ")
        for v in self._graph[e]:
            if v[0] not in q.list and v[0] not in op:
                q.enqueue(v[0])
        op.append(e)
        self._bfs(q,op)

    def numberOfSCC(self):
        '''Find total number of strongly connected components. (Only for undirected right now)'''
        visited = set()
        count = 0
        for k in self._graph.keys():
            if not k in visited:
                count += 1
                self.DFSUtil(k,visited)
        print("Total number of SCCs is {}".format(count))
        return count

    def floyd_warshall_algorithm(self):
        print("Floyd Warshall starting up...")
        sleep(1)
        n = len(self._graph)
        dist = []*n
        index_map = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}
        for i in range(n):
            l = [float("inf")]*n
            l[i] = 0
            dist.append(l)

        for k in self._graph:
            edges = self._graph[k]
            i = index_map[k]

            for e in edges:
                print(e)
                edge = e[0]
                weight = e[1]
                j = index_map[edge]

                try:
                    dist[i][j] = weight
                except IndexError:
                    print("Error with max {}".format(n))
                    print(i,j)


        for k in range(n):
            for i in range(n):
                for j in range(n):
                    current_distance = dist[i][j]
                    new_distance = dist[i][k] + dist[k][j]
                    if current_distance > new_distance:
                        dist[i][j] = new_distance

        for i in dist:
            print(i)

    def performDijkstra(self, source):
        print("Running Dijkstra's algorithm in O(mlogn)...")
        sleep(2)

        # Holds the vertices we know the shortest paths to
        X = [source]

        # Holds the shortest path lengths from source to key in the dict
        D = {source: 0}

        # i = 0
        # Keep looping until all nodes have been discovered
        while len(X) < len(self._graph):
        # while i < 2:
            # i += 1

            # Find the smallest outgoing from the frontier
            min = float("inf")
            minEdge = None

            for sourceVertex in X:
                # print("Checking source - {}".format(sourceVertex))
                for endVertex, weight in self._graph[sourceVertex]:
                    # print("Checking destination - {}".format(endVertex))
                    if endVertex not in X:
                        prevWeight = 0
                        if D[sourceVertex]:
                            prevWeight += D[sourceVertex]
                        w = prevWeight + weight
                        if w < min:
                            # print("Found min with vertex {}".format(endVertex))
                            min = w
                            minEdge = (endVertex, w)
                    # else:
                        # print("Skipping {} since already discovered".format(endVertex))
            if minEdge:
                v, w = minEdge
                X.append(v)
                D[v] = w
            # print("Length of X is {}".format(len(X)))
        return D




def testWeightedGraph():
    graph_connections = [('A', 'B', 4), ('A', 'C', 1), ('A', 'E', 5), ('B', 'A', 4), ('B', 'D', 1),
                         ('C', 'A', 1), ('C', 'D', 1), ('C', 'F', 2), ('D', 'B', 1), ('D', 'C', 1),
                         ('E', 'A', 4), ('E', 'F', 1), ('F', 'C', 2), ('F', 'E', 1)]
    g = Graph(False)
    g.addConnections(graph_connections)
    g.showGraph()
    sourceVertex = 'A'
    # print("Shortest paths from source {} is {} ".format(sourceVertex, g.performDijkstra(sourceVertex)))
    # g.performBFS()
    g.depthFirstSearch()
    return g


def testGraph():
    print("Here's a graph for free!\n")
    connections = [('A', 'B', 3), ('B', 'C', 1), ('B', 'D', 2),
                   ('C', 'D', 4), ('E', 'F', 5), ('F', 'C', 5),('A','E',2)]
    is_directed = False
    g = Graph(is_directed)
    g.addConnections(connections)
    g.performBFS()
    # g.floyd_warshall_algorithm()
    return g
