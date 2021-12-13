import networkx as nx

from GramatykiGrafoweAGH import Node
from GramatykiGrafoweAGH.exceptions import NodeNotFoundError, CannotApplyProductionError, SquareNotFoundError
from GramatykiGrafoweAGH.utils import get_first_node_with_label, get_square_vertices, replace_node


def make_initial_graph() -> nx.Graph:
    G = nx.Graph()
    E = Node(label='E', x=0.5, y=0.5, level=0)
    G.add_node(E)
    return G


def P1(G: nx.Graph) -> None:
    try:
        E = get_first_node_with_label(G, 'E')
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


def P2(G: nx.Graph) -> None:
    try:
        I = get_first_node_with_label(G, 'I')
    except NodeNotFoundError:
        raise CannotApplyProductionError()

    level = I.level

    try:
        E1, E2, E3, E4 = get_square_vertices(G, I)
    except SquareNotFoundError:
        raise CannotApplyProductionError()

    x1, y1 = E1.x, E1.y
    x2, y2 = E2.x, E2.y
    x3, y3 = E3.x, E3.y
    x4, y4 = E4.x, E4.y

    x5, y5 = (x1 + x2) / 2, (y1 + y2) / 2
    x6, y6 = (x1 + x3) / 2, (y1 + y3) / 2
    x7, y7 = (x2 + x4) / 2, (y2 + y4) / 2
    x8, y8 = (x3 + x4) / 2, (y3 + y4) / 2
    x9, y9 = (x1 + x4) / 2, (y1 + y4) / 2

    i = Node(label='i', x=I.x, y=I.y, level=level)

    I1 = Node(label='I', x=(x1 + x9) / 2, y=(y1 + y9) / 2, level=level + 1)
    I2 = Node(label='I', x=(x2 + x9) / 2, y=(y2 + y9) / 2, level=level + 1)
    I3 = Node(label='I', x=(x3 + x9) / 2, y=(y3 + y9) / 2, level=level + 1)
    I4 = Node(label='I', x=(x4 + x9) / 2, y=(y4 + y9) / 2, level=level + 1)

    E1 = Node(label='E', x=x1, y=y1, level=level + 1)
    E2 = Node(label='E', x=x2, y=y2, level=level + 1)
    E3 = Node(label='E', x=x3, y=y3, level=level + 1)
    E4 = Node(label='E', x=x4, y=y4, level=level + 1)
    E5 = Node(label='E', x=x5, y=y5, level=level + 1)
    E6 = Node(label='E', x=x6, y=y6, level=level + 1)
    E7 = Node(label='E', x=x7, y=y7, level=level + 1)
    E8 = Node(label='E', x=x8, y=y8, level=level + 1)
    E9 = Node(label='E', x=x9, y=y9, level=level + 1)

    replace_node(G, I, i)

    G.add_nodes_from([
        I1, I2, I3, I4,
        E1, E2, E3, E4, E5, E6, E7, E8, E9,
    ])

    G.add_edges_from([
        (i, I1), (i, I2), (i, I3), (i, I4),
        (I1, E1), (I1, E5), (I1, E9), (I1, E6),
        (I2, E5), (I2, E2), (I2, E7), (I2, E9),
        (I3, E6), (I3, E9), (I3, E8), (I3, E3),
        (I4, E9), (I4, E7), (I4, E4), (I4, E8),
        (E1, E5), (E5, E2),
        (E1, E6), (E5, E9), (E2, E7),
        (E6, E9), (E9, E7),
        (E6, E3), (E9, E8), (E7, E4),
        (E3, E8), (E8, E4),
    ])
