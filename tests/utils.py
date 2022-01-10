from GramatykiGrafoweAGH import Graph, Node


def make_P11_left_side_graph():
    G = Graph()

    level = 2

    E = Node(label='E', x=0, y=0, level=level)
    iL = Node(label='i', x=-1, y=-1, level=level)
    iR = Node(label='i', x=1, y=-1, level=level)

    I1L = Node(label='I', x=-2, y=-2, level=level + 1)
    I2L = Node(label='I', x=-1, y=-2, level=level + 1)

    I1R = Node(label='I', x=1.5, y=-2, level=level + 1)

    E1L = Node(label='E', x=0, y=-3, level=level + 1)
    E2L = Node(label='E', x=0, y=-4, level=level + 1)
    E3L = Node(label='E', x=0, y=-5, level=level + 1)

    E1R = Node(label='E', x=0, y=-3, level=level + 1)
    E3R = Node(label='E', x=0, y=-5, level=level + 1)

    G.add_nodes([E, iL, iR, I1L, I2L, I1R, E1L, E2L, E3L, E1R, E3R])

    G.add_edges([
        (E, iL), (E, iR), (iL, I1L), (iL, I2L), (iR, I1R),
        (I1L, E1L), (I1L, E2L), (I2L, E2L), (I2L, E3L),
        (I1R, E1R),
        (E1L, E2L), (E2L, E3L), (E1R, E3R),
        (I1R, E1R), (I1R, E3R)
    ])

    return G


def make_P12_left_side_graph():
    G = Graph()

    level = 2

    E = Node(label='E', x=0, y=0, level=level)
    iL = Node(label='i', x=-1, y=-1, level=level)
    iR = Node(label='i', x=1, y=-1, level=level)

    I1L = Node(label='I', x=-2, y=-2, level=level + 1)
    I2L = Node(label='I', x=-1, y=-2, level=level + 1)

    I1R = Node(label='I', x=1.5, y=-2, level=level + 1)

    E1L = Node(label='E', x=0, y=-3, level=level + 1)
    E2L = Node(label='E', x=0, y=-4, level=level + 1)
    E3L = Node(label='E', x=0, y=-5, level=level + 1)

    E3R = Node(label='E', x=0, y=-5, level=level + 1)

    G.add_nodes([E, iL, iR, I1L, I2L, I1R, E1L, E2L, E3L, E3R])

    G.add_edges([
        (E, iL), (E, iR), (iL, I1L), (iL, I2L), (iR, I1R),
        (I1L, E1L), (I1L, E2L), (I2L, E2L), (I2L, E3L),
        (I1R, E1L),
        (E1L, E2L), (E2L, E3L), (E1L, E3R),
        (I1R, E1L), (I1R, E3R)
    ])

    return G
