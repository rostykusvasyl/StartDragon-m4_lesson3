#! /usr/bin/python3


def bfs(graph, start):
    visited, verticies = [], [start_vertex]
    while verticies:
        vertex = verticies.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            verticies.extend([v for v in graph[vertex]
                                if  v not in visited])
    return visited


def add_graph_vertex(graph, vertex, edges):
    '''Adds  vertex to graph.'''
    if not edges:
        graph[vertex] = []
    edges = edges.split(',')
    if vertex in graph:
        for edge in edges:
            if edge not in graph[vertex]:
                graph[vertex].append(edge)
    else:
        graph[vertex] = edges

    for edge in edges:
        if edge in graph:
            graph[edge].append(vertex)
        else:
            graph[edge] = [vertex]


graph = {}

while True:
    vertex = input("Please enter graph vertex: ")
    if not vertex:
        continue

    edges = input(f"Please input edges separated by ',' for {vertex}: ")
    add_graph_vertex(graph, vertex, edges)
    print(graph)
    next_vertex = input("Stop adding verticies? (y/yes)."
                        " Press enter for continue: ")

    if next_vertex.lower() in ('y', 'yes'):
        break

while True:
    start_vertex = input("Please input start vertex: ")
    if start_vertex:
        print(bfs(graph, start_vertex))
    else:
        break
