from time import time

from GramatykiGrafoweAGH.project.task1 import make_initial_graph, P1, P2
from GramatykiGrafoweAGH.project.task4 import P7
from GramatykiGrafoweAGH.project.task5 import P8
from GramatykiGrafoweAGH.project.task6 import P9

if __name__ == '__main__':
    G = make_initial_graph()

    start = time()

    G.apply_productions([P1, P2])

    G.assert_no_duplicated_nodes()

    G.apply_production(P2, times=4)
    G.apply_production_while_possible(P7)
    G.apply_production_while_possible(P8)

    G.assert_no_duplicated_nodes()

    G.apply_production(P2, times=16)
    G.apply_production_while_possible(P7)
    G.apply_production_while_possible(P8)
    G.apply_production_while_possible(P9)

    G.assert_no_duplicated_nodes()

    G.apply_production(P2, times=64)
    G.apply_production_while_possible(P7)
    G.apply_production_while_possible(P8)
    G.apply_production_while_possible(P9)

    G.assert_no_duplicated_nodes()

    end = time()
    print(end - start)

    G.show()
