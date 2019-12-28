import numpy as np


def down_eta_constructor(bool_omega_g_basis, vertices):
    down_eta = {}
    
    edge_basis = bool_omega_g_basis[vertices:]

    for row in edge_basis:
        down_eta[tuple(row)] = True

    for row in edge_basis:
        # The list() here avoids dict change size error
        for key in list(down_eta):
            try:
                down_eta[tuple(row+list(key))]
            except:
                down_eta[tuple(row+list(key))] = True
    
    # Adding the empty set 
    down_eta[tuple(np.zeros(len(bool_omega_g_basis[0])))] = True

    down_eta_array = np.array(list(down_eta))
    
    return down_eta_array

def up_eta_constructor(bool_omega_g_basis, vertices):
    up_eta = {}
    
    # Constructing the top of down_eta to be joined with the vertex basis
    down_eta_top = np.zeros(len(bool_omega_g_basis[0]))
    np.put(down_eta_top, range(vertices,len(down_eta_top)), 1) 
    down_eta_top = down_eta_top.astype(bool)

    vertex_basis = bool_omega_g_basis[:vertices]

    for row in vertex_basis:
        up_eta[tuple(row+down_eta_top)] = True

    for row in vertex_basis:
        # The list() here avoids dict cahnge size error
        for key in list(up_eta):
            try:
                up_eta[tuple(row+list(key))]
            except:
                up_eta[tuple(row+list(key))] = True
    print(up_eta, "\n", len(up_eta))

    up_eta_array = np.array(list(up_eta))
    print(up_eta_array)

    return up_eta_array

def sus_omega_g_constructor(bool_omega_g_basis, vertices):
    
    return

def omega_g_constructor(omega_g_basis, vertices):
    # cache = {}
    omega_g = {}
    bool_omega_g_basis = omega_g_basis.astype(bool)
    
    # Every omega_g is composed of the following 3 parts:
    #   1.) down_eta
    #   2.) up_eta
    #   3.) sus(omega_g)
    #   We construct each one individually and concat at the end.

    down_eta = down_eta_constructor(bool_omega_g_basis, vertices)
    up_eta = up_eta_constructor(bool_omega_g_basis, vertices)
    sus_omega_g = sus_omega_g_constructor(bool_omega_g_basis, vertices)

    for i, row in enumerate(bool_omega_g_basis):
        temp = bool_omega_g_basis[i]
        for j in range(i+1, len(omega_g_basis)):
            omega_g[tuple(temp + bool_omega_g_basis[j])] = True
            print(temp + bool_omega_g_basis[j])
    
    # Possible approach:
    #   1.) Construct down_eta
    #   2.) Construct up_eta
    #   3.) Construct sus(omega_g)

    return omega_g


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

    omega_g = omega_g_constructor(omega_g_basis, vertices)

    print("Graph:\n", graph)
    print("Edge num:", edges)
    print("Vert num:", len(graph))
    print("Omega_g Basis (vertices + edges):\n", omega_g_basis)
    print("Omega_g:\n", omega_g)
    
    return

if __name__ == "__main__":
    main()
