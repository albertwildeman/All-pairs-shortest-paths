import numpy as np


def floyd_warshall(n_nodes, n_edges, edges):

    # Rename nodes to start at 0
    node_namebase = edges[:,:2].min()
    edges[:, :2] -= node_namebase

    # Determine the sum of all edge lengths, to serve as infinity (no path can ever be this long)
    # for later comparisons
    max_length = sum(edges[:,2])

    # Initialize 3-dimensional array to hold shortest path from node i to node j, using only the first k
    # nodes
    a = np.zeros((n_nodes, n_nodes, n_nodes+1), dtype=np.float64)

    # Set values of a for k=0
    # First, set all to infinity (this is valid only when i and j are distinct and there is no edge between them).
    a[:,:,0] = max_length

    # Set the diagonal (in i-j sense; keep k at 0) entries to 0, as the distance from any node to itself is 0.
    np.fill_diagonal(a[:,:,0], 0)

    # Iterate over the edgesQ
    for i_edge in range(n_edges):
        tail, head, length = edges[i_edge, :]
        a[tail, head, 0] = min(a[tail, head, 0], length)

    # Iterate over the prefix-subset of all nodes
    for k in range(1, n_nodes+1):

        if k%10==0:
            print("Working k %s of %s..." % (k, n_nodes))

        # Iterate over the start node
        for i in range(n_nodes):
            # Iterate over the end node
            for j in range(n_nodes):
                a[i, j, k] = min(a[i, j, k-1], a[i, k-1, k-1] + a[k-1, j, k-1])

    shortest_paths = a[:, :, n_nodes]

    if min( np.diagonal( shortest_paths ) < 0 ):
        neg_cycle_exists = True
    else:
        neg_cycle_exists = False

    return shortest_paths, neg_cycle_exists
