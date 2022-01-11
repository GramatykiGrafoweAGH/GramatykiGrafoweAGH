from typing import Tuple

from GramatykiGrafoweAGH import Node, Graph
from GramatykiGrafoweAGH.exceptions import NodeNotFoundError, CannotApplyProductionError, SquareNotFoundError


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
        E1, E2, E3, E4 = get_square_vertices_local(G, I)
    except SquareNotFoundError:
        raise CannotApplyProductionError()

    try:
        E12 = next(G.get_common_neighbors_with_label(E1, E2, 'E'))
        E13 = next(G.get_common_neighbors_with_label(E1, E3, 'E'))
        E24 = next(G.get_common_neighbors_with_label(E2, E4, 'E'))
    except StopIteration:
        raise CannotApplyProductionError()

    next_level = level + 1

    x1, y1 = E1.x, E1.y
    x2, y2 = E2.x, E2.y
    x3, y3 = E3.x, E3.y
    x4, y4 = E4.x, E4.y
    x12, y12 = E12.x, E12.y
    x13, y13 = E13.x, E13.y
    x24, y24 = E24.x, E24.y

    x34, y34 = (x3 + x4) / 2, (y3 + y4) / 2
    x14, y14 = (x1 + x4) / 2, (y1 + y4) / 2

    i = Node(label='i', x=I.x, y=I.y, level=level)

    I1 = Node(label='I', x=(x1 + x14) / 2, y=(y1 + y14) / 2, level=next_level)
    I2 = Node(label='I', x=(x2 + x14) / 2, y=(y2 + y14) / 2, level=next_level)
    I3 = Node(label='I', x=(x3 + x14) / 2, y=(y3 + y14) / 2, level=next_level)
    I4 = Node(label='I', x=(x4 + x14) / 2, y=(y4 + y14) / 2, level=next_level)

    E1 = Node(label='E', x=x1, y=y1, level=next_level)
    E2 = Node(label='E', x=x2, y=y2, level=next_level)
    E3 = Node(label='E', x=x3, y=y3, level=next_level)
    E4 = Node(label='E', x=x4, y=y4, level=next_level)
    E12 = Node(label='E', x=x12, y=y12, level=next_level)
    E13 = Node(label='E', x=x13, y=y13, level=next_level)
    E24 = Node(label='E', x=x24, y=y24, level=next_level)
    E34 = Node(label='E', x=x34, y=y34, level=next_level)
    E14 = Node(label='E', x=x14, y=y14, level=next_level)

    G.replace_node(I, i)

    G.add_nodes([
        I1, I2, I3, I4,
        E1, E2, E3, E4, E12, E13, E24, E34, E14,
    ])

    G.add_edges([
        (i, I1), (i, I2), (i, I3), (i, I4),
        (I1, E1), (I1, E12), (I1, E13), (I1, E14),
        (I2, E2), (I2, E12), (I2, E24), (I2, E14),
        (I3, E3), (I3, E13), (I3, E34), (I3, E14),
        (I4, E4), (I4, E24), (I4, E34), (I4, E14),
        (E12, E1), (E12, E2),
        (E13, E1), (E13, E3),
        (E24, E2), (E24, E4),
        (E34, E3), (E34, E4),
        (E14, E12), (E14, E13), (E14, E24), (E14, E34),
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
        E1, E2, E3, E4 = get_square_vertices_local(G, I)
    except SquareNotFoundError:
        raise CannotApplyProductionError()

    try:
        E12 = next(G.get_common_neighbors_with_label(E1, E2, 'E'))
        E13 = next(G.get_common_neighbors_with_label(E1, E3, 'E'))
        E24 = next(G.get_common_neighbors_with_label(E2, E4, 'E'))
        E34 = next(G.get_common_neighbors_with_label(E3, E4, 'E'))
    except StopIteration:
        raise CannotApplyProductionError()

    next_level = level + 1

    x1, y1 = E1.x, E1.y
    x2, y2 = E2.x, E2.y
    x3, y3 = E3.x, E3.y
    x4, y4 = E4.x, E4.y
    x12, y12 = E12.x, E12.y
    x13, y13 = E13.x, E13.y
    x24, y24 = E24.x, E24.y
    x34, y34 = E34.x, E34.y

    x14, y14 = (x1 + x4) / 2, (y1 + y4) / 2

    i = Node(label='i', x=I.x, y=I.y, level=level)

    I1 = Node(label='I', x=(x1 + x14) / 2, y=(y1 + y14) / 2, level=next_level)
    I2 = Node(label='I', x=(x2 + x14) / 2, y=(y2 + y14) / 2, level=next_level)
    I3 = Node(label='I', x=(x3 + x14) / 2, y=(y3 + y14) / 2, level=next_level)
    I4 = Node(label='I', x=(x4 + x14) / 2, y=(y4 + y14) / 2, level=next_level)

    E1 = Node(label='E', x=x1, y=y1, level=next_level)
    E2 = Node(label='E', x=x2, y=y2, level=next_level)
    E3 = Node(label='E', x=x3, y=y3, level=next_level)
    E4 = Node(label='E', x=x4, y=y4, level=next_level)
    E12 = Node(label='E', x=x12, y=y12, level=next_level)
    E13 = Node(label='E', x=x13, y=y13, level=next_level)
    E24 = Node(label='E', x=x24, y=y24, level=next_level)
    E34 = Node(label='E', x=x34, y=y34, level=next_level)
    E14 = Node(label='E', x=x14, y=y14, level=next_level)

    G.replace_node(I, i)

    G.add_nodes([
        I1, I2, I3, I4,
        E1, E2, E3, E4, E12, E13, E24, E34, E14,
    ])

    G.add_edges([
        (i, I1), (i, I2), (i, I3), (i, I4),
        (I1, E1), (I1, E12), (I1, E13), (I1, E14),
        (I2, E2), (I2, E12), (I2, E24), (I2, E14),
        (I3, E3), (I3, E13), (I3, E34), (I3, E14),
        (I4, E4), (I4, E24), (I4, E34), (I4, E14),
        (E12, E1), (E12, E2),
        (E13, E1), (E13, E3),
        (E24, E2), (E24, E4),
        (E34, E3), (E34, E4),
        (E14, E12), (E14, E13), (E14, E24), (E14, E34),
    ])
