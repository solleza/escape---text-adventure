
from adjacencygraph import *

def bfs(graph, start):
    '''template bfs. Returns None
    '''
    reached = dict()
    queue = []

    reached[start] = start
    queue.append(start)

    while queue:
        v = queue.pop(0)

        for w in graph.neighbours(v):
            if w not in reached:
                reached[w] = v
                queue.append(w)

    return None

def get_next_v(graph, start, dest):
    '''Finds the shortest path from start to dest in graph and returns the next
    vertex you should take if you're taking two steps towards the shortest path.

    Args:
        graph(UndirectedAdjacencyGraph): The digraph defining the edges between
            the vertices.

        start: The vertex where the path starts. It is assumed that start is a
            vertex of graph.

        dest:  The vertex where the path ends. It is assumed that dest is a
            vertex of graph.

    Returns:
        vertex: The next vertex you should take for the shortest path

    '''
    if dest in graph.neighbours(start):
        return dest

    reached = dict()
    queue = []

    reached[start] = start
    queue.append(start)

    while queue:
        v = queue.pop(0)

        if dest in graph.neighbours(v):
            reached[dest] = v
            break

        for w in graph.neighbours(v):
            if w not in reached:
                reached[w] = v
                queue.append(w)

    path = [ dest ]
    v = dest
    while not reached[v] == start:
        v = reached[v]
        path.insert(0,v)
    path.insert(0,start)

    return path[2]

def get_farthest(graph, start):
    '''Finds the farthest vertex in graph from start

    Args:
        graph(AdjacencyGraph): The digraph defining the edges between the vertices.

        start: The vertex where the path starts. It is assumed that start is a
            vertex of graph.

    Returns:
        vertex: farthest vertex in graph from start
    '''
    reached = dict()
    queue = []

    reached[start] = (0, start) # (weight, prev)
    queue.append(start)

    while queue:
        v = queue.pop(0)
        weight = reached[v][0]

        for w in graph.neighbours(v):
            if w not in reached:
                reached[w] = (weight + 1, v)
                queue.append(w)

    l = []
    for v in reached:
        l.append( (reached[v][0], v) )
    l.sort(key=lambda x:x[0], reverse=True)
    result = l.pop(0)

    return result[1]
