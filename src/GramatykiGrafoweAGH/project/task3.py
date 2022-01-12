from typing import Tuple

from GramatykiGrafoweAGH import Node, Graph
from GramatykiGrafoweAGH.exceptions import NodeNotFoundError, CannotApplyProductionError, SquareNotFoundError
from GramatykiGrafoweAGH.project.utils import get_square_vertices_extended


def make_initial_graph_P5(graph_type) -> Graph:
    G = Graph()

    I = Node(label='I', x=0, y=0, level=1)
    E1 = Node(label='E', x=-.5, y=.5, level=1)
    E2 = Node(label='E', x=.5, y=.5, level=1)
    E3 = Node(label='E', x=-.5, y=-.5, level=1)
    E4 = Node(label='E', x=.5, y=-.5, level=1)

    E_a = Node(label='E', x=0, y=.5, level=1)
    E_b = Node(label='E', x=.5, y=0, level=1)
    E_c = Node(label='E', x=0, y=-.5, level=1)
    E_d = Node(label='E', x=-.5, y=0, level=1)

    edges = [(I, E1), (I, E2), (I, E3), (I, E4)]

    if graph_type == 0:
        G.add_nodes([I, E1, E2, E3, E4, E_a, E_b, E_c])
        edges += [
            (E1, E_a), (E_a, E2),
            (E2, E_b), (E_b, E4),
            (E4, E_c), (E_c, E3),
            (E3, E1),
        ]
    if graph_type == 1:
        G.add_nodes([I, E1, E2, E3, E4, E_a, E_b, E_d])
        edges += [
            (E1, E_a), (E_a, E2),
            (E2, E_b), (E_b, E4),
            (E4, E3),
            (E3, E_d), (E_d, E1),
        ]
    if graph_type == 2:
        G.add_nodes([I, E1, E2, E3, E4, E_a, E_c, E_d])
        edges += [
            (E1, E_a), (E_a, E2),
            (E2, E4),
            (E4, E_c), (E_c, E3),
            (E3, E_d), (E_d, E1),
        ]
    if graph_type == 3:
        G.add_nodes([I, E1, E2, E3, E4, E_b, E_c, E_d])
        edges += [
            (E1, E2),
            (E2, E_b), (E_b, E4),
            (E4, E_c), (E_c, E3),
            (E3, E_d), (E_d, E1),
        ]

    G.add_edges(edges)

    return G


def get_square_vertices_local(G: Graph, I: Node) -> Tuple[Node, Node, Node, Node]:
    Es = G.get_neighbors_with_label(I, 'E')
    if len(Es) != 4:
        raise SquareNotFoundError()

    E3 = min(Es, key=lambda node: (node.x, node.y))
    Es.remove(E3)
    E2 = max(Es, key=lambda node: (node.x, node.y))
    Es.remove(E2)
    E4 = max(Es, key=lambda node: node.x)
    Es.remove(E4)
    E1, = Es

    return E1, E2, E3, E4


def P5(G: Graph) -> None:
    try:
        I = G.get_first_node_with_label('I')
    except NodeNotFoundError:
        raise CannotApplyProductionError()

    level = I.level

    try:
        [E00, E02, E22, E20], edges = get_square_vertices_extended(G, I)
    except SquareNotFoundError:
        raise CannotApplyProductionError()

    eCount = len(list(filter(lambda x: x is not None, edges)))
    if eCount != 3:
        raise CannotApplyProductionError()

    E01 = edges[0]
    E12 = edges[1]
    E21 = edges[2]

    next_level = level + 1

    x00, y00 = E00.x, E00.y
    x02, y02 = E02.x, E02.y
    x20, y20 = E20.x, E20.y
    x22, y22 = E22.x, E22.y

    x01, y01 = E01.x, E01.y
    x12, y12 = E12.x, E12.y
    x21, y21 = E21.x, E21.y

    x10, y10 = (x00 + x20) / 2, (y00 + y20) / 2
    x11, y11 = (x00 + x22) / 2, (y00 + y22) / 2

    i = Node(label='i', x=I.x, y=I.y, level=level)

    I00 = Node(label='I', x=(x00 + x11 + x10 + x01) / 4, y=(y00 + y11 + y10 + y01) / 4, level=next_level)
    I01 = Node(label='I', x=(x02 + x11 + x01 + x12) / 4, y=(y02 + y11 + y01 + y12) / 4, level=next_level)
    I10 = Node(label='I', x=(x20 + x11 + x21 + x10) / 4, y=(y20 + y11 + y21 + y10) / 4, level=next_level)
    I11 = Node(label='I', x=(x22 + x11 + x21 + x12) / 4, y=(y22 + y11 + y21 + y12) / 4, level=next_level)

    E00 = Node(label='E', x=x00, y=y00, level=next_level)
    E01 = Node(label='E', x=x01, y=y01, level=next_level)
    E02 = Node(label='E', x=x02, y=y02, level=next_level)
    E10 = Node(label='E', x=x10, y=y10, level=next_level)
    E11 = Node(label='E', x=x11, y=y11, level=next_level)
    E12 = Node(label='E', x=x12, y=y12, level=next_level)
    E20 = Node(label='E', x=x20, y=y20, level=next_level)
    E21 = Node(label='E', x=x21, y=y21, level=next_level)
    E22 = Node(label='E', x=x22, y=y22, level=next_level)

    G.replace_node(I, i)

    G.add_nodes([
        I00, I01, I10, I11,
        E00, E01, E02,
        E10, E11, E12,
        E20, E21, E22
    ])

    G.add_edges([
        (i, I00), (i, I01), (i, I10), (i, I11),
        (I00, E00), (I00, E01), (I00, E10), (I00, E11),
        (I01, E02), (I01, E01), (I01, E12), (I01, E11),
        (I10, E20), (I10, E10), (I10, E21), (I10, E11),
        (I11, E22), (I11, E12), (I11, E21), (I11, E11),

        (E00, E01), (E01, E02),
        (E10, E11), (E11, E12),
        (E20, E21), (E21, E22),

        (E00, E10), (E10, E20),
        (E01, E11), (E11, E21),
        (E02, E12), (E12, E22),
    ])


def make_initial_graph_P6() -> Graph:
    G = Graph()

    I = Node(label='I', x=0, y=0, level=1)
    E1 = Node(label='E', x=-.5, y=.5, level=1)
    E2 = Node(label='E', x=.5, y=.5, level=1)
    E3 = Node(label='E', x=-.5, y=-.5, level=1)
    E4 = Node(label='E', x=.5, y=-.5, level=1)
    E12 = Node(label='E', x=0, y=.5, level=1)
    E13 = Node(label='E', x=-.5, y=0, level=1)
    E24 = Node(label='E', x=.5, y=0, level=1)
    E34 = Node(label='E', x=0, y=-.5, level=1)

    G.add_nodes([I, E1, E2, E3, E4, E12, E13, E24, E34])

    G.add_edges([
        (I, E1), (I, E2), (I, E3), (I, E4),
        (E1, E12), (E1, E13),
        (E2, E12), (E2, E24),
        (E3, E13), (E3, E34),
        (E4, E24), (E4, E34),
    ])

    return G


def P6(G: Graph) -> None:
    try:
        I = G.get_first_node_with_label('I')
    except NodeNotFoundError:
        raise CannotApplyProductionError()

    level = I.level

    try:
        [E00, E02, E22, E20], edges = get_square_vertices_extended(G, I)
    except SquareNotFoundError:
        raise CannotApplyProductionError()

    eCount = len(list(filter(lambda x: x is not None, edges)))
    if eCount != 4:
        raise CannotApplyProductionError()

    E01 = edges[0]
    E12 = edges[1]
    E21 = edges[2]
    E10 = edges[3]

    next_level = level + 1

    x00, y00 = E00.x, E00.y
    x02, y02 = E02.x, E02.y
    x20, y20 = E20.x, E20.y
    x22, y22 = E22.x, E22.y

    x01, y01 = E01.x, E01.y
    x12, y12 = E12.x, E12.y
    x21, y21 = E21.x, E21.y
    x10, y10 = E10.x, E10.y

    x11, y11 = (x00 + x22) / 2, (y00 + y22) / 2

    i = Node(label='i', x=I.x, y=I.y, level=level)

    I00 = Node(label='I', x=(x00 + x11 + x10 + x01) / 4, y=(y00 + y11 + y10 + y01) / 4, level=next_level)
    I01 = Node(label='I', x=(x02 + x11 + x01 + x12) / 4, y=(y02 + y11 + y01 + y12) / 4, level=next_level)
    I10 = Node(label='I', x=(x20 + x11 + x21 + x10) / 4, y=(y20 + y11 + y21 + y10) / 4, level=next_level)
    I11 = Node(label='I', x=(x22 + x11 + x21 + x12) / 4, y=(y22 + y11 + y21 + y12) / 4, level=next_level)

    E00 = Node(label='E', x=x00, y=y00, level=next_level)
    E01 = Node(label='E', x=x01, y=y01, level=next_level)
    E02 = Node(label='E', x=x02, y=y02, level=next_level)
    E10 = Node(label='E', x=x10, y=y10, level=next_level)
    E11 = Node(label='E', x=x11, y=y11, level=next_level)
    E12 = Node(label='E', x=x12, y=y12, level=next_level)
    E20 = Node(label='E', x=x20, y=y20, level=next_level)
    E21 = Node(label='E', x=x21, y=y21, level=next_level)
    E22 = Node(label='E', x=x22, y=y22, level=next_level)

    G.replace_node(I, i)

    G.add_nodes([
        I00, I01, I10, I11,
        E00, E01, E02,
        E10, E11, E12,
        E20, E21, E22
    ])

    G.add_edges([
        (i, I00), (i, I01), (i, I10), (i, I11),
        (I00, E00), (I00, E01), (I00, E10), (I00, E11),
        (I01, E02), (I01, E01), (I01, E12), (I01, E11),
        (I10, E20), (I10, E10), (I10, E21), (I10, E11),
        (I11, E22), (I11, E12), (I11, E21), (I11, E11),

        (E00, E01), (E01, E02),
        (E10, E11), (E11, E12),
        (E20, E21), (E21, E22),

        (E00, E10), (E10, E20),
        (E01, E11), (E11, E21),
        (E02, E12), (E12, E22),
    ])
