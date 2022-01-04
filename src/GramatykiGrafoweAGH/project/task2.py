from GramatykiGrafoweAGH import Node, Graph
from GramatykiGrafoweAGH.exceptions import NodeNotFoundError, CannotApplyProductionError, SquareNotFoundError
from GramatykiGrafoweAGH.project.utils import get_square_vertices


def P3(G: Graph) -> None:
    try:
        I = G.get_first_node_with_label('I')
    except NodeNotFoundError:
        raise CannotApplyProductionError()

    level = I.level

    try:
        E1, E2, E3, E4 = get_square_vertices(G, I)
    except SquareNotFoundError:
        raise CannotApplyProductionError()

    try:
        E13 = next(G.get_common_neighbors_with_label(E1, E3, 'E'))
    except StopIteration:
        raise CannotApplyProductionError()

    next_level = level + 1

    x1, y1 = E1.x, E1.y
    x2, y2 = E2.x, E2.y
    x3, y3 = E3.x, E3.y
    x4, y4 = E4.x, E4.y
    x13, y13 = E13.x, E13.y

    x12, y12 = (x1 + x2) / 2, (y1 + y2) / 2
    x34, y34 = (x3 + x4) / 2, (y3 + y4) / 2
    x14, y14 = (x1 + x4) / 2, (y1 + y4) / 2
    x24, y24 = (x2 + x4) / 2, (y2 + y4) / 2

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


def P4(G: Graph) -> None:
    try:
        I = G.get_first_node_with_label('I')
    except NodeNotFoundError:
        raise CannotApplyProductionError()

    level = I.level

    try:
        E1, E2, E3, E4 = get_square_vertices(G, I)
    except SquareNotFoundError:
        raise CannotApplyProductionError()

    try:
        E12 = next(G.get_common_neighbors_with_label(E1, E2, 'E'))
        E13 = next(G.get_common_neighbors_with_label(E1, E3, 'E'))
    except StopIteration:
        raise CannotApplyProductionError()

    next_level = level + 1

    x1, y1 = E1.x, E1.y
    x2, y2 = E2.x, E2.y
    x3, y3 = E3.x, E3.y
    x4, y4 = E4.x, E4.y
    x12, y12 = E12.x, E12.y
    x13, y13 = E13.x, E13.y

    x34, y34 = (x3 + x4) / 2, (y3 + y4) / 2
    x14, y14 = (x1 + x4) / 2, (y1 + y4) / 2
    x24, y24 = (x2 + x4) / 2, (y2 + y4) / 2

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
