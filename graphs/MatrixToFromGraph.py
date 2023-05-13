from Graph import Graph
def matrix_to_graph_plug(matrix):
    vertex_num = len(matrix)
    if (vertex_num != len(matrix[0]) or vertex_num == 0):
        raise Exception("Sorry, matrix have to be square matrix")
    g1_edges_from_node = {}
    # Outgoing edges from the node: (adjacent_node, cost) in graph 1.
    for i in range(0, vertex_num):
        count = 0
        a = []
        for weight in matrix[i]:
            if (weight != 0):
                a.append((count, weight))
            count += 1
        g1_edges_from_node[i] = a

    g = Graph(0, g1_edges_from_node)

    return g


def MST_to_matrix_plug(MST):
    size = len(MST)
    if (size == 0):
        raise Exception("ERROR, call 'matrix_MST' function first")
    matrix = []
    for i in range(0, size):
        a = [0] * size
        for v in MST:
            if (v[0] != None and v[0] == i):
                a[v[1]] = v[2]
        matrix.append(a)

    return matrix

