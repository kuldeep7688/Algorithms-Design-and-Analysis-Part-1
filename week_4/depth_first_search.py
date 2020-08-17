from collections import deque


# dfs using stacks
def depth_first_search_using_stack(graph, starting_vertex):
    unexplored_boolean_dict = {
        key: True
        for key in graph.keys()
    }
    vertex_stack = deque()
    vertex_stack.append(starting_vertex)
    unexplored_boolean_dict[starting_vertex] = False
    while len(vertex_stack) > 0:
        current_vertex = vertex_stack.pop()
        for connected_vertex in graph[current_vertex]:
            if unexplored_boolean_dict[connected_vertex] is True:
                vertex_stack.append(connected_vertex)
                unexplored_boolean_dict[connected_vertex] = False
                print("going through edge {}--{}".format(current_vertex, connected_vertex))
        print()
    return


# dfs using recursion
def depth_first_search_using_recursion(graph, starting_vertex, unexplored_boolean_dict):
    unexplored_boolean_dict[starting_vertex] = False
    for connected_vertex in graph[starting_vertex]:
        if unexplored_boolean_dict[connected_vertex] is True:
            depth_first_search_using_recursion(graph, connected_vertex, unexplored_boolean_dict)
            print("going through edge {}--{}".format(starting_vertex, connected_vertex))
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
    depth_first_search_using_stack(graph, 's')
    print()
    unexplored_boolean_dict = {
        key: True
        for key in graph.keys()
    }
    depth_first_search_using_recursion(graph, 's', unexplored_boolean_dict)
