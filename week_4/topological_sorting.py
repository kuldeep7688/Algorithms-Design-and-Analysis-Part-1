from pprint import pprint

# topological sort
def dfs_for_topological_sort(graph, starting_vertex):
    global topo_order, current_order, unexplored_boolean_dict
    unexplored_boolean_dict[starting_vertex] = False
    for connected_vertex in graph[starting_vertex]:
        if unexplored_boolean_dict[connected_vertex] is True:
            dfs_for_topological_sort(graph, connected_vertex)
    topo_order[starting_vertex] = current_order
    current_order -= 1
    return


def topological_sort(graph):
    global topo_order
    global current_order
    global unexplored_boolean_dict

    for vertex in graph.keys():
        if unexplored_boolean_dict[vertex] is True:
            dfs_for_topological_sort(graph, vertex)

    return


if __name__ == "__main__":
    graph_dict_directed_acyclic = {
        's' : ['a', 'b'],
        'a' : ['c'],
        'b' : ['c', 'd'],
        'c' : ['e', 'd'],
        'd' : ['e'],
        'e' : []
    }
    pprint(graph_dict_directed_acyclic)

    topo_order = {}
    current_order = len(graph_dict_directed_acyclic.keys())
    unexplored_boolean_dict = {
        key: True
        for key in graph_dict_directed_acyclic.keys()
    }
    topological_sort(graph_dict_directed_acyclic)
    pprint(topo_order)
