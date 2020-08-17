from collections import deque


# bfs using queue
def breadth_first_search(graph, starting_vertex):
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
                print("going through edge {}--{}".format(current_vertex, connected_vertex))
        print()
    return


if __name__ == "__main__":
    graph = {
        's' : ['a', 'b'],
        'a' : ['s', 'c'],
        'b' : ['s', 'c', 'd'],
        'c' : ['a', 'e', 'b', 'd'],
        'd' : ['b', 'c', 'e'],
        'e' : ['c', 'd']
    }
    breadth_first_search(graph, 's')
