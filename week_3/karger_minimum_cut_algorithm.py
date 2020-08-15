import random
from tqdm import tqdm
from pprint import pprint
import math
from copy import deepcopy


def delete_edge_and_update_graph(v1, v2, g):
    """
    Merges the edges of the selected edge and updates the graph.
    Args:
        v1 (variable): first vertext of the edge to merge
        v2 (variable): second vertext of the edge to merge
        graph (dict): graph
    Returns:
        dict: updated graph
    """
    g[v1].extend(g[v2])
    del g[v2]
    # replacing all v2 with v1 in graph
    for vertex, edges in g.items():
        g[vertex] = [edge if edge != v2 else v1 for edge in edges]
    # removing self loops
    g[v1] = [edge for edge in g[v1] if edge != v1]

    return g


def random_minimum_cut(g):
    """
    Identifies a probable minimum cut in the given graph.
    Args:
        g (dict): graph
    Returns:
        int: number of crossing edges in the selected cut
    """
    while len(list(g.keys())) > 2:
        # get random edge
        v1 = list(g.keys())[random.randint(0, len(g.keys()) - 1)]
        v2 = g[v1][random.randint(0, len(g[v1]) - 1)]
        # delete the edge in graph and update
        g = delete_edge_and_update_graph(v1, v2, g)
    return len(g[list(g.keys())[0]])


def maximize_probability_of_identifying_a_minimum_cut(graph):
    all_minimum_cuts = []
    total_number_of_vertices_in_graph = len(graph.keys())
    minimum_number_of_trials = math.ceil((total_number_of_vertices_in_graph**2)*math.log(total_number_of_vertices_in_graph))

    for _ in tqdm(range(minimum_number_of_trials)):
        all_minimum_cuts.append(
            random_minimum_cut(deepcopy(graph))
        )
    return min(all_minimum_cuts)


if __name__ == "__main__":
    graph = {
        1: [2, 3, 4, 7],
        2: [1, 3, 4],
        3: [1, 2, 4],
        4: [1, 2, 3, 5],
        5: [4, 6, 7, 8],
        6: [5, 7, 8],
        7: [1, 5, 6, 8],
        8: [5, 6, 7]
    }
    pprint("Input graph to the algorithm is : {}".format(graph))
    minimum_cuts_crossing_edges = maximize_probability_of_identifying_a_minimum_cut(
        graph
    )
    pprint("The number of crossing edges in the minimum cut of the input graph is {}".format(minimum_cuts_crossing_edges))
