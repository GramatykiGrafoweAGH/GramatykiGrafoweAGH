from GramatykiGrafoweAGH.project import make_initial_graph, P1, P2
from GramatykiGrafoweAGH.utils import apply_productions, check_duplicated_nodes
from GramatykiGrafoweAGH.visualization import show_graph

if __name__ == '__main__':
    G = make_initial_graph()
    G = apply_productions(G, [P1, P2, P2, P2, P2, P2])
    check_duplicated_nodes(G)
    show_graph(G)
