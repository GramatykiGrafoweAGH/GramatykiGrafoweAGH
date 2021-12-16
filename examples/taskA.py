from GramatykiGrafoweAGH.project.task1 import make_initial_graph, P1, P2
from GramatykiGrafoweAGH.project.task4 import P7
from GramatykiGrafoweAGH.project.task5 import P8

if __name__ == '__main__':
    G = make_initial_graph()

    G.apply_production(P1)
    G.apply_production(P2, times=5)
    G.apply_production(P7, times=3)
    G.apply_production(P8)

    G.assert_no_duplicated_nodes()
    G.show()
