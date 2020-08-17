from tqdm import tqdm
from pprint import pprint


def prepare_a_reverse_graph(graph):
    g = {
        key: []
        for key in graph.keys()
    }
    for key, val in graph.items():
        for v in val:
            g[v].append(key)
    return g


def dfs_finishing_time_loop(graph, vertex):
    global unexplored_boolean_dict, current_time, finishing_times_list

    unexplored_boolean_dict[vertex] = False
    for connected_vertex in graph[vertex]:
        if unexplored_boolean_dict[connected_vertex] is True:
            dfs_finishing_time_loop(graph, connected_vertex)

    current_time += 1
    finishing_times_list.append((current_time, vertex))
    return


def dfs_assigning_leader(graph, vertex):
    global leader_to_all_vertices_dict, current_leader

    unexplored_boolean_dict[vertex] = False
    leader_to_all_vertices_dict[current_leader].append(vertex)
    for connected_vertex in graph[vertex]:
        if unexplored_boolean_dict[connected_vertex] is True:
            dfs_assigning_leader(graph, connected_vertex)
    return


def kosaraju_strongly_connected_components_of_a_graph(graph):
    global current_time, unexplored_boolean_dict, finishing_times_list
    global leader_to_all_vertices_dict, current_leader

    # 1st pass computing finishing times
    graph_rev = prepare_a_reverse_graph(graph)
    for vertex in tqdm(graph_rev.keys()):
        if unexplored_boolean_dict[vertex] is True:
            dfs_finishing_time_loop(graph_rev, vertex)

    del graph_rev
    # resetting unexplored
    for key in unexplored_boolean_dict.keys():
        unexplored_boolean_dict[key] = True

    finishing_times_list  = sorted(finishing_times_list, reverse=True)
    for ti, vertex in tqdm(finishing_times_list):
        if unexplored_boolean_dict[vertex] is True:
            current_leader = vertex
            leader_to_all_vertices_dict[current_leader] = []
            dfs_assigning_leader(graph, vertex)

    return


if __name__ == "__main__":
    graph = {
        1: [2],
        2: [6, 3, 4],
        3: [1, 4],
        4: [5],
        5: [4],
        6: [5, 7],
        7: [6, 8],
        8: [5, 7],
    }
    pprint(graph)
    unexplored_boolean_dict = {
        key: True
        for key in graph.keys()
    }
    finishing_times_list = []
    current_time = 0
    leader_to_all_vertices_dict = {}
    current_leader = None
    kosaraju_strongly_connected_components_of_a_graph(graph)
    pprint(leader_to_all_vertices_dict)
