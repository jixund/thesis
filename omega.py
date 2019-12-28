import numpy as np


def edge_basis(omega_g_basis, vertices):
    """
    The rows in omega_g_basis whose indeces are greater than the number of vertices are the edge basis rows.
    """
    for i in range(0, vertices):
        omega_g_basis[vertices+i][vertices+i] = 1

    return omega_g_basis

def vertex_basis(graph, omega_g_basis, vertices):
    """
    The first n rows in omega_g_basis are the vertex basis rows, where n is the number of vertices.
    """

    for i, row in enumerate(graph):
        # The ith entry of the ith row should be a 1, denoting the particular vertex.
        omega_g_basis[i][i] = 1
        # The ith row greater than n is a copy of the ith row of the adjacency matrix.
        omega_g_basis[i][vertices:] = row

    return omega_g_basis

def main():
    graph = np.array([[0,1,1], [1,0,1], [1,1,0]])
    vertices = len(graph)
    edges = np.sum([np.sum(row[i+1:]) for i, row in enumerate(graph)])
    
    omega_g_basis = np.zeros((vertices+edges, vertices+edges))
    omega_g_basis = vertex_basis(graph, omega_g_basis, vertices)
    omega_g_basis = edge_basis(omega_g_basis, vertices)

    print("Graph:\n", graph)
    print("Edge num:", edges)
    print("Vert num:", len(graph))
    print("Omega_g Basis (vertices + edges):\n", omega_g_basis)
    
    return

if __name__ == "__main__":
    main()
