import math
from collections import deque


def shortest_distance(graph, starting_vertex, ending_vertex):
    distance_from_starting_vertex_dict = {
        key : math.inf
        for key in graph.keys()
    }
    distance_from_starting_vertex_dict[starting_vertex] = 0
    unexplored_boolean_dict = {
        key: True
        for key in graph.keys()
    }
    vertex_queue = deque()
    vertex_queue.append(starting_vertex)
    unexplored_boolean_dict[starting_vertex] = False
    while len(vertex_queue) > 0:
        current_vertex = vertex_queue.popleft()
        for connected_vertex in graph[current_vertex]:
            if unexplored_boolean_dict[connected_vertex] is True:
                vertex_queue.append(connected_vertex)
                unexplored_boolean_dict[connected_vertex] = False
                distance_from_starting_vertex_dict[connected_vertex] = distance_from_starting_vertex_dict[current_vertex] + 1
    return distance_from_starting_vertex_dict[ending_vertex]


if __name__ == "__main__":
    graph = {
        's' : ['a', 'b'],
        'a' : ['s', 'c'],
        'b' : ['s', 'c', 'd'],
        'c' : ['a', 'e', 'b', 'd'],
        'd' : ['b', 'c', 'e'],
        'e' : ['c', 'd']
    }
    print(shortest_distance(graph, 's', 'e'))
