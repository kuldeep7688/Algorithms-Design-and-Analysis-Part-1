import math
from tqdm import tqdm
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
    with open("/media/rabbit/Work_data/github_projects/Algorithms-Design-and-Analysis-Part-1/week_5/assignment/dijkstraData.txt") as inp:
        lines = inp.readlines()
    lines = [l.strip() for l in lines]
    graph = {}
    for line in tqdm(lines):
        v1, edges = int(line.split()[0]), line.split()[1:]
        graph[(v1)] = []
        for edge in edges:
            vertex, edge_weight = edge.strip().split(',')
            graph[v1].append((int(vertex), int(edge_weight)))

    del lines
    starting_vertex = 1
    shortest_distances_from_starting_vertex = dijsktra_shortest_path_algorithm(graph, starting_vertex)
    ending_vertices = [7,37,59,82,99,115,133,165,188,197]
    for ending_vertex in ending_vertices:
        print(
            "Shortest Distance from {} to {} is {}".format(
                starting_vertex, ending_vertex,
                shortest_distances_from_starting_vertex[ending_vertex]
            )
        )
