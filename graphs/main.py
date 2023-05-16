import Matrix_Plug
import PrintGraph


start = 1
# matrix = [[0, 1, 2, 1, 1, 2, 1],
#           [1, 0, 2, 0, 0, 0, 2],
#           [2, 2, 0, 1, 0, 0, 0],
#           [1, 0, 1, 0, 2, 0, 0],
#           [1, 0, 0, 2, 0, 2, 0],
#           [2, 0, 0, 0, 2, 0, 1],
#           [1, 0, 2, 0, 0, 1, 0]]
matrix = [[0, 2, 12, 0, 0],
          [0, 0, 8, 0, 9],
          [0, 0, 0, 6, 3],
          [10, 0, 0, 0, 4],
          [0, 4, 0, 2, 0]]


G = Matrix_Plug.matrix_to_graph_plug(matrix, start)
PrintGraph.print_graph(matrix)
PrintGraph.print_graph(Matrix_Plug.MST_to_matrix_plug(G.Prim_MST()))
PrintGraph.print_graph(Matrix_Plug.MST_to_matrix_plug(G.Dijkstra_MST()))

