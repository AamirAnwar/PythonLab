import sys
from collections import defaultdict

class Graph(object):

    def __init__(self, directed, connections):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self,connections):
        '''Adding connections between a list of vertex tuples'''
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        '''Adding connection between two vertices'''
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

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
                newPath = self.findPath(graph,node,end,path)
            if newPath:
                return newPath
        return None