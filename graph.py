import sys
from collections import defaultdict
from time import sleep
class Graph(object):

    def __init__(self, directed, connections):
        self._graph = defaultdict(list)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self,connections):
        '''Adding connections between a list of vertex tuples'''
        for node1, node2, weight in connections:
            self.add(node1, node2, weight)

    def add(self, node1, node2, weight):
        '''Adding connection between two vertices'''
        self._graph[node1].append({node2:weight})
        if not self._directed:
            self._graph[node2].append({node1:weight})

    def remove(self, node):
        '''Remove a node from the graph'''
        for n, con in self._graph.items():
            try:
                con.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_adjacent(self, node1, node2):
        '''Are these two nodes adjacent?'''
        return node1 in self._graph and node2 in self._graph[node1]


    def __str__(self):
        '''Helpful in debugging'''
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

    def findPath(self, start, end, path=[]):
        ''' Find a path between two nodes.This uses backtracking and aggresively pursues unconquered territory'''
        path = path + [start]
        if start == end:
            return path
        if not self._graph[start]:
            return None
        for node in self._graph[start]:
            if node not in path:
                newPath = self.findPath(node,end,path)
            if newPath:
                return newPath
        return None


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
                edge =list(e.keys())[0]
                weight = list(e.values())[0]
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




def testGraph():
    print("Here's a graph for free!\n")
    connections = [('A', 'B', 3), ('B', 'C', 1), ('B', 'D', 2),
                   ('C', 'D', 4), ('E', 'F', 5), ('F', 'C', 5),('A','E',2)]
    is_directed = False
    g = Graph(is_directed, connections)
    print("Floyd Warshall starting up...")
    sleep(1)
    g.floyd_warshall_algorithm()
    return g
