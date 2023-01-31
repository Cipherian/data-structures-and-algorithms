class Graph:

    def __init__(self):
        self.adj_list = []


    def __str__(self):
        return [vertex.value for vertex in self.adj_list]

    def size(self):
       return len(self.adj_list)

    def add_node(self, value: any)-> any:
        new_vertex = Vertex(value)
        self.adj_list.append(new_vertex)
        return new_vertex

    def get_nodes(self):
        return self.adj_list

    def add_edge(self, start: str, vertex: str, weight: int = 0):
        if start not in self.adj_list or vertex not in self.adj_list:
            raise KeyError("Both 'start' and 'vertex' must be present in the graph.")

        new_edge = Edge(vertex, weight)
        for node in self.adj_list:
            if node == start:
                node.neighbors.append(new_edge)

    def get_neighbors(self, vertex):
        for node in self.adj_list:
            if node == vertex:
                return node.neighbors



class Vertex:
    def __init__(self, value, neighbors = None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        return self.value

class Edge:

    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    def __str__(self):
        return self.vertex.value

