from GramatykiGrafoweAGH.project.task1 import make_initial_graph, P1, P2
from GramatykiGrafoweAGH.utils import apply_productions, assert_no_duplicated_nodes
from GramatykiGrafoweAGH.visualization import show_graph

if __name__ == '__main__':
    G = make_initial_graph()
    G = apply_productions(G, [P1, P2, P2, P2, P2, P2])
    # assert_no_duplicated_nodes(G)  # currently will fail
    show_graph(G)
