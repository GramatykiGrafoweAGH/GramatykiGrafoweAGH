from GramatykiGrafoweAGH.project.task1 import make_initial_graph, P1, P2
from GramatykiGrafoweAGH.project.task4 import P7
from GramatykiGrafoweAGH.project.taskC import P10, P11, P12

if __name__ == '__main__':
    G = make_initial_graph()

    G.apply_productions([
        P1, P2,
        P10, P2, P2, P2,
        P7, P11, P7, P12,
    ])

    G.assert_no_duplicated_nodes()
    G.show()
