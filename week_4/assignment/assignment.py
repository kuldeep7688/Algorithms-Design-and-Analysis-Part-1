from collections import deque
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


def dfs_finishing_time_loop_using_stack(graph, starting_vertex):
    global unexplored_boolean_dict, current_time, finishing_times_list

    vertex_stack = deque()
    vertex_stack.append(starting_vertex)
    unexplored_boolean_dict[starting_vertex] = False
    popped_items = deque()
    while len(vertex_stack) > 0:
        current_vertex = vertex_stack.pop()
        popped_items.append(current_vertex)
        for connected_vertex in graph[current_vertex]:
            if unexplored_boolean_dict[connected_vertex] is True:
                vertex_stack.append(connected_vertex)
                unexplored_boolean_dict[connected_vertex] = False

    for _ in range(len(popped_items)):
        vertex = popped_items.pop()
        current_time += 1
        finishing_times_list.append((current_time, vertex))
    return


def dfs_assigning_leader_using_stack(graph, starting_vertex):
    global leader_to_all_vertices_dict, current_leader

    vertex_stack = deque()
    vertex_stack.append(starting_vertex)
    unexplored_boolean_dict[starting_vertex] = False
    popped_items = deque()
    while len(vertex_stack) > 0:
        current_vertex = vertex_stack.pop()
        popped_items.append(current_vertex)
        for connected_vertex in graph[current_vertex]:
            if unexplored_boolean_dict[connected_vertex] is True:
                vertex_stack.append(connected_vertex)
                unexplored_boolean_dict[connected_vertex] = False

    for _ in range(len(popped_items)):
        leader_to_all_vertices_dict[starting_vertex].append(popped_items.pop())
    return


def kosaraju_strongly_connected_components_of_a_graph_using_stacks(graph):
    global current_time, unexplored_boolean_dict, finishing_times_list
    global leader_to_all_vertices_dict, current_leader

    # 1st pass computing finishing times
    graph_rev = prepare_a_reverse_graph(graph)
    print("reversed graph prepared.")
    print("Finding finishing times.")
    for vertex in tqdm(graph_rev.keys()):
        if unexplored_boolean_dict[vertex] is True:
            dfs_finishing_time_loop_using_stack(graph_rev, vertex)

    del graph_rev
    print("1st pass complete.")
    # resetting unexplored
    for key in unexplored_boolean_dict.keys():
        unexplored_boolean_dict[key] = True

    finishing_times_list = sorted(finishing_times_list, reverse=True)
    for ti, vertex in tqdm(finishing_times_list):
        if unexplored_boolean_dict[vertex] is True:
            current_leader = vertex
            leader_to_all_vertices_dict[current_leader] = []
            dfs_assigning_leader_using_stack(graph, vertex)
    return


if __name__ == "__main__":
    with open("/media/rabbit/Work_data/github_projects/Algorithms-Design-and-Analysis-Part-1/week_4/assignment/SCC.txt") as inp:
        lines = inp.readlines()
    print("Total edges in the graph are : {}".format(len(lines)))
    graph = {
        key: []
        for key in range(1, 875715)
    }
    for line in tqdm(lines):
        v1, v2 = line.strip().split()
        graph[int(v1.strip())].append(int(v2.strip()))

    del lines
    unexplored_boolean_dict = {
        key: True
        for key in graph.keys()
    }
    finishing_times_list = []
    current_time = 0
    leader_to_all_vertices_dict = {}
    current_leader = None

    print("starting algorithm....")
    kosaraju_strongly_connected_components_of_a_graph_using_stacks(graph)
    print("Size of top 10 largest SCC are : {}".format(sorted([len(val) for val in leader_to_all_vertices_dict.values()], reverse=True)[:10]))
