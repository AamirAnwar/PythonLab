import graph
print("Welcome to Python Lab!")

print("Here's a graph for free!\n\n")
connections = [('A', 'B'), ('B', 'C'), ('B', 'D'),
               ('C', 'D'), ('E', 'F'), ('F', 'C')]
g = graph.Graph(False, connections)
print(g._graph.items())

