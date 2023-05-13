import  MatrixToFromGraph
import PrintGraph
matrix = [[0, 1, 2, 1, 1, 2, 1],
          [1, 0, 2, 0, 0, 0, 2],
          [2, 2, 0, 1, 0, 0, 0],
          [1, 0, 1, 0, 2, 0, 0],
          [1, 0, 0, 2, 0, 2, 0],
          [2, 0, 0, 0, 2, 0, 1],
          [1, 0, 2, 0, 0, 1, 0]]
G = MatrixToFromGraph.matrix_to_graph_plug(matrix)

PrintGraph.print_graph(matrix)
PrintGraph.print_graph(MatrixToFromGraph.MST_to_matrix_plug(G.Prim_MST()))
PrintGraph.print_graph(MatrixToFromGraph.MST_to_matrix_plug(G.Dijkstra_MST()))
