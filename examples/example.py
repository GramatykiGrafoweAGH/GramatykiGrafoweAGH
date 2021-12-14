from GramatykiGrafoweAGH.project.task1 import make_initial_graph, P1, P2

if __name__ == '__main__':
    G = make_initial_graph()
    G.apply_productions([P1, P2])
    G.assert_no_duplicated_nodes()
    G.show()
