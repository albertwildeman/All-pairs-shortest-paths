from FileReadLib import get_data
from FloydWarshallLib import floyd_warshall

n_graphs = 3

# for i_graph in range(n_graphs):
for i_graph in range(1):

    filename = "g" + str(i_graph+1)
    n_nodes, n_edges, edges = get_data(filename)

    shortest_shortest_path = [[] for x in range(n_graphs)]

    # To determine the shortest shortest path, run the Floyd-Warshall algorithm
    local_shortest_paths = floyd_warshall(n_nodes, n_edges, edges)

    shortest_shortest_path[i_graph] = min(shortest_path)

