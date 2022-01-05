from GramatykiGrafoweAGH import Graph
from GramatykiGrafoweAGH.project.task1 import make_initial_graph, P1, P2
from GramatykiGrafoweAGH.project.taskC import P10

if __name__ == '__main__':
    G = make_initial_graph()

    G.apply_productions([P1, P2])

    def run_driver(G: Graph, last_level: int) -> None:
        assert last_level >= 2

        for level in range(2, last_level):
            G.apply_production(P10, times=(1 << level) - 2)
            G.apply_production(P2, times=1 << (level - 1))

            # TODO: apply proper productions
            # G.apply_production_while_possible(P7)
            # G.apply_production_while_possible(P8)
            # G.apply_production_while_possible(P9)
            # G.apply_production_while_possible(P11)
            # G.apply_production_while_possible(P12)

    last_level = 5
    run_driver(G, last_level)

    # G.assert_no_duplicated_nodes()  # TODO: fix duplicates
    G.show(level=last_level, mark_duplicates=True)
