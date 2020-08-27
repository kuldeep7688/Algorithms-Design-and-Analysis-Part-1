import math
from pprint import pprint


def dijsktra_shortest_path_algorithm(graph, start_vertex):
    """
    Dijkstra Implementation without using heaps.
    Args:
        graph (dict): graph with edge weights.

    Returns:
        dict: returns the dict containing shortest distance of all edges with the starting_vertex
    """
    total_number_vertices = len(graph)

    shortest_distance_dict = {start_vertex: 0}
    vertices_passed_so_far = set([start_vertex])

    while len(vertices_passed_so_far) < total_number_vertices:
        minimum_distance = math.inf
        minimum_distance_connected_vertex = None
        for vertex in vertices_passed_so_far:
            for connected_vertex, edge_distance in graph[vertex]:
                if connected_vertex not in vertices_passed_so_far:
                    temp_distance = shortest_distance_dict[vertex] + edge_distance
                    if minimum_distance > temp_distance:
                        minimum_distance = temp_distance
                        minimum_distance_connected_vertex = connected_vertex

        shortest_distance_dict[minimum_distance_connected_vertex] = minimum_distance
        vertices_passed_so_far.add(minimum_distance_connected_vertex)
    return shortest_distance_dict


if __name__ == "__main__":
    graph = {
        1: [(2,9), (3,2), (4,6)],
        2: [(6, 4)],
        3: [(4,3), (5,1)],
        4: [(2,2), (6,7), (7, 9)],
        5: [(8, 6), (4, 1)],
        6: [(7, 1), (9, 5)],
        7: [(9,1), (8, 5)],
        8: [(9, 5)],
        9: []
    }
    print("The graph on which dijkstra operate is given below :")
    pprint(graph)
    print()
    starting_vertex = 1
    shortest_distances_from_starting_vertex = dijsktra_shortest_path_algorithm(graph, starting_vertex)
    for key, value in shortest_distances_from_starting_vertex.items():
        print("Shortest Distance from {} to {} is {}".format(starting_vertex, key, value))
