import networkx as nx
import matplotlib.pyplot as plt


def print_graph(matrix):
    vertex_num = len(matrix)
    if( vertex_num == len(matrix[0])):
        G = nx.Graph()
        for i in range(1,vertex_num+1):
            count = 1
            for j in matrix[i-1]:
                if(j != 0):
                    print(i, '***', count)
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


G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]
print_graph(G)
