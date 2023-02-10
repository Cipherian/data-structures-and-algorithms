from data_structures.graph import Graph


def direct_flights(graph: Graph, cities: list):
    cost = 0
    for i in range(len(cities) - 1):
        start_city = cities[i]
        end_city = cities[i + 1]

        start_vertex = None
        end_vertex = None
        for vertex in graph.get_nodes():
            if vertex.value == start_city:
                start_vertex = vertex
            if vertex.value == end_city:
                end_vertex = vertex

        if not start_vertex or not end_vertex:
            return False, cost

        edge_exists = False
        for neighbor in start_vertex.neighbors:
            if neighbor.vertex == end_vertex:
                edge_exists = True
                cost += neighbor.weight
                break

        if not edge_exists:
            return False, cost

    return edge_exists, cost

