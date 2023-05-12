import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Dict  # For annotations


MST = []


class Node:

    def __init__(self, arg_id):
        self.parent = None
        self._id = arg_id


class Graph:

    def __init__(self, source: int, adj_list: Dict[int, List[int]]):
        self.source = source
        self.adjlist = adj_list

    def PrimsMST(self) -> int:

        # Priority queue is implemented as a dictionary with
        # key as an object of 'Node' class and value as the cost of
        # reaching the node from the source.
        # Since the priority queue can have multiple entries for the
        # same adjacent node but a different cost, we have to use objects as
        # keys so that they can be stored in a dictionary.
        # [As dictionary can't have duplicate keys so objectify the key]

        # The distance of source node from itself is 0. Add source node as the first node
        # in the priority queue
        priority_queue = {Node(self.source): 0}
        added = [False] * len(self.adjlist)
        min_span_tree_cost = 0

        while priority_queue:
            # Choose the adjacent node with the least edge cost
            node = min(priority_queue, key=priority_queue.get)  # min priority queue
            cost = priority_queue[node]

            # Remove the node from the priority queue
            del priority_queue[node]

            if added[node._id] == False:
                min_span_tree_cost += cost
                added[node._id] = True
                print("Added Node : " + str(node._id) + ", cost now : " + str(min_span_tree_cost) +", Parent Node : " + str(node.parent) + ", Edge weight : " + str(cost))
                MST.append([node.parent, node._id, cost])

                for item in self.adjlist[node._id]:
                    adjnode = item[0]
                    adjcost = item[1]
                    if added[adjnode] == False:
                        vertex = Node(adjnode)
                        priority_queue[vertex] = adjcost
                        vertex.parent = node._id
        return min_span_tree_cost


def matrix_MST(matrix):
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

    # g1_edges_from_node[0] = [(1, 1), (2, 2), (3, 1), (4, 1), (5, 2), (6, 1)]
    # g1_edges_from_node[1] = [(0, 1), (2, 2), (6, 2)]
    # g1_edges_from_node[2] = [(0, 2), (1, 2), (3, 1)]
    # g1_edges_from_node[3] = [(0, 1), (2, 1), (4, 2)]
    # g1_edges_from_node[4] = [(0, 1), (3, 2), (5, 2)]
    # g1_edges_from_node[5] = [(0, 2), (4, 2), (6, 1)]
    # g1_edges_from_node[6] = [(0, 1), (2, 2), (5, 1)]

    g1 = Graph(0, g1_edges_from_node)
    cost = g1.PrimsMST()
    print("Cost of the minimum spanning tree in graph 1 : " + str(cost) + "\n")


def graph_matrix_plug(array):
    size = len(array)
    if (size == 0):
        raise Exception("ERROR, call 'matrix_MST' function first")
    matrix = []
    for i in range(0, size):
        a = [0] * size
        for v in array:
            if (v[0] != None and v[0] == i):
                a[v[1]] = v[2]
        matrix.append(a)

    return matrix


def print_graph(matrix):
    vertex_num = len(matrix)
    if( vertex_num == len(matrix[0])):
        G = nx.Graph()
        for i in range(1,vertex_num+1):
            count = 1
            for j in matrix[i-1]:
                if(j != 0):
                    G.add_edge(i, count, weight=j)
                count += 1
        elarge = [(u, v) for (u, v, d) in G.edges(data=True)]
        pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility
        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=700)
        # edges
        nx.draw_networkx_edges(G, pos, edgelist=elarge, width=2)
        # node labels
        nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
        # edge weight labels
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()


matrix = [[0, 1, 2, 1, 1, 2, 1],
          [1, 0, 2, 0, 0, 0, 2],
          [2, 2, 0, 1, 0, 0, 0],
          [1, 0, 1, 0, 2, 0, 0],
          [1, 0, 0, 2, 0, 2, 0],
          [2, 0, 0, 0, 2, 0, 1],
          [1, 0, 2, 0, 0, 1, 0]]
matrix_MST(matrix)
print_graph(matrix)
print_graph(graph_matrix_plug(MST))
