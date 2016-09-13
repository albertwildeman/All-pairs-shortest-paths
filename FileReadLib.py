import os
import numpy as np


def get_data(filename):

    filepath = os.getcwd() + "\\" + filename + ".txt"
    file_array = open(filepath)


    raw_lines = [x[:-1].split(" ") for x in file_array.readlines()]
    n_nodes = int(raw_lines[0][0])
    n_edges = int(raw_lines[0][1])
    edges = np.array([(int(x), int(y), int(z)) for x, y, z in raw_lines[1:]])

    file_array.close()

    return n_nodes, n_edges, edges

