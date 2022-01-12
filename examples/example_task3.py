from GramatykiGrafoweAGH.project.task3 import make_initial_graph_P5, P5, make_initial_graph_P6, P6

if __name__ == '__main__':
    G = make_initial_graph_P5(1)
    G.apply_productions([P5])
    G.assert_no_duplicated_nodes()
    G.show()

    G = make_initial_graph_P5(2)
    G.apply_productions([P5])
    G.assert_no_duplicated_nodes()
    G.show()

    G = make_initial_graph_P5(3)
    G.apply_productions([P5])
    G.assert_no_duplicated_nodes()
    G.show()

    G = make_initial_graph_P6()
    G.apply_productions([P6])
    G.assert_no_duplicated_nodes()
    G.show()
