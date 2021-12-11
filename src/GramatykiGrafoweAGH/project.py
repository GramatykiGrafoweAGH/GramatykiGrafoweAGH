import networkx as nx

from GramatykiGrafoweAGH import Node, production
from GramatykiGrafoweAGH.exceptions import NodeNotFoundError, CannotApplyProductionError
from GramatykiGrafoweAGH.utils import find_node_with_label, replace_node


def make_initial_graph() -> nx.Graph:
    G = nx.Graph()
    E = Node(label='E', x=0.5, y=0.5, level=0)
    G.add_node(E)
    return G


@production
def P1(G: nx.Graph):
    try:
        E = find_node_with_label(G, 'E')
    except NodeNotFoundError:
        raise CannotApplyProductionError()

    x0 = E.x
    y0 = E.y
    level = E.level

    x1, y1 = x0 - 0.5, y0 - 0.5
    x2, y2 = x0 + 0.5, y0 - 0.5
    x3, y3 = x0 - 0.5, y0 + 0.5
    x4, y4 = x0 + 0.5, y0 + 0.5

    e = Node(label='e', x=x0, y=y0, level=level)
    I = Node(label='I', x=x0, y=y0, level=level + 1)
    E1 = Node(label='E', x=x1, y=y1, level=level + 1)
    E2 = Node(label='E', x=x2, y=y2, level=level + 1)
    E3 = Node(label='E', x=x3, y=y3, level=level + 1)
    E4 = Node(label='E', x=x4, y=y4, level=level + 1)

    replace_node(G, E, e)

    G.add_nodes_from([I, E1, E2, E3, E4])

    G.add_edges_from([
        (e, I),
        (I, E1), (I, E2), (I, E3), (I, E4),
        (E1, E2), (E2, E4), (E4, E3), (E3, E1),
    ])
