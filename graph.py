import sys

# Define a graph as such
g = {'A':['B'],
         'B':['A','D'],
         'C': ['B'],
         'D':['C']
         }

# Depth first search. This uses backtracking and aggresively pursues unconquered territory
def findPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph[start]:
        return None
    for node in graph[start]:
        if node not in path:
            newPath = findPath(graph,node,end,path)
            if newPath:
                return newPath
    return None

print(findPath(g,'A','C'))