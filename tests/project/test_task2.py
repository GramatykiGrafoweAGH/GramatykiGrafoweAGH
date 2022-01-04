from GramatykiGrafoweAGH import Graph, Node
from GramatykiGrafoweAGH.project.task2 import P3, P4
from GramatykiGrafoweAGH.testing import assert_production_cannot_be_applied


def make_initial_graph_P3() -> Graph:
    G = Graph()

    I = Node(label='I', x=0, y=0, level=1)
    E1 = Node(label='E', x=-.5, y=.5, level=1)
    E2 = Node(label='E', x=.5, y=.5, level=1)
    E3 = Node(label='E', x=-.5, y=-.5, level=1)
    E4 = Node(label='E', x=.5, y=-.5, level=1)
    E13 = Node(label='E', x=-.5, y=0, level=1)

    G.add_nodes([I, E1, E2, E3, E4, E13])

    G.add_edges([
        (I, E1), (I, E2), (I, E3), (I, E4),
        (E1, E2),
        (E2, E4),
        (E1, E13), (E13, E3),
        (E3, E4),
    ])

    return G


def make_initial_graph_P4() -> Graph:
    G = Graph()

    I = Node(label='I', x=0, y=0, level=1)
    E1 = Node(label='E', x=-.5, y=.5, level=1)
    E2 = Node(label='E', x=.5, y=.5, level=1)
    E3 = Node(label='E', x=-.5, y=-.5, level=1)
    E4 = Node(label='E', x=.5, y=-.5, level=1)
    E12 = Node(label='E', x=0, y=.5, level=1)
    E13 = Node(label='E', x=-.5, y=0, level=1)

    G.add_nodes([I, E1, E2, E3, E4, E12, E13])

    G.add_edges([
        (I, E1), (I, E2), (I, E3), (I, E4),
        (E1, E12), (E1, E13),
        (E2, E12), (E2, E4),
        (E3, E13), (E3, E4),
    ])

    return G


def make_right_side_graph_P3():
    G = Graph()

    level = 1

    x0, y0 = 0, 0
    x1, y1 = -0.5, -0.5
    x2, y2 = 0.5, -0.5
    x3, y3 = -0.5, 0.5
    x4, y4 = 0.5, 0.5
    x5, y5 = 0.0, -0.5
    x6, y6 = -0.5, 0.0
    x7, y7 = 0.5, 0.0
    x8, y8 = 0.0, 0.5
    x9, y9 = 0.0, 0.0

    x13, y13 = -0.5, 0

    i = Node(label='i', x=x0, y=y0, level=level)
    E1 = Node(label='E', x=x1, y=y1, level=level)
    E2 = Node(label='E', x=x2, y=y2, level=level)
    E3 = Node(label='E', x=x3, y=y3, level=level)
    E4 = Node(label='E', x=x4, y=y4, level=level)

    E13 = Node(label='E', x=x13, y=y13, level=level)

    G.add_nodes([i, E1, E2, E3, E4, E13])

    G.add_edges([
        (i, E1), (i, E2), (i, E3), (i, E4),
        (E13, E1), (E13, E3),
        (E3, E4),
        (E2, E4),
        (E1, E2),
    ])

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

    G.add_nodes([
        I1, I2, I3, I4,
        E1, E2, E3, E4, E5, E6, E7, E8, E9,
    ])

    G.add_edges([
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

    return G


def make_right_side_graph_P4():
    G = Graph()

    level = 1

    x0, y0 = 0, 0
    x1, y1 = -0.5, -0.5
    x2, y2 = 0.5, -0.5
    x3, y3 = -0.5, 0.5
    x4, y4 = 0.5, 0.5
    x5, y5 = 0.0, -0.5
    x6, y6 = -0.5, 0.0
    x7, y7 = 0.5, 0.0
    x8, y8 = 0.0, 0.5
    x9, y9 = 0.0, 0.0

    x13, y13 = -0.5, 0
    x34, y34 = 0, 0.5

    i = Node(label='i', x=x0, y=y0, level=level)
    E1 = Node(label='E', x=x1, y=y1, level=level)
    E2 = Node(label='E', x=x2, y=y2, level=level)
    E3 = Node(label='E', x=x3, y=y3, level=level)
    E4 = Node(label='E', x=x4, y=y4, level=level)

    E13 = Node(label='E', x=x13, y=y13, level=level)
    E34 = Node(label='E', x=x34, y=y34, level=level)

    G.add_nodes([i, E1, E2, E3, E4, E13, E34])

    G.add_edges([
        (i, E1), (i, E2), (i, E3), (i, E4),
        (E13, E1), (E13, E3),
        (E34, E3), (E34, E4),
        (E2, E4),
        (E1, E2),
    ])

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

    G.add_nodes([
        I1, I2, I3, I4,
        E1, E2, E3, E4, E5, E6, E7, E8, E9,
    ])

    G.add_edges([
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

    return G


def test_P3_isomorphic_left_side():
    # test application of P3 to the graph isomorphic to left side of P3
    G = make_initial_graph_P3()
    expected = make_right_side_graph_P3()

    P3(G)

    assert G.is_isomorphic_with(expected)


def test_P3_left_side_deleted_node():
    # test application of P3 to the graph isomorphic to left side of P3 with deleted one node
    G = make_initial_graph_P3()
    E = G.get_first_node_with_label('E')
    G.remove_node(E)

    assert_production_cannot_be_applied(P3, G)


def test_P3_left_side_deleted_edge():
    # test application of P3 to the graph isomorphic to left side of P3 with deleted one edge
    G = make_initial_graph_P3()
    E = G.get_first_node_with_label('E')
    G.remove_edge(E, list(G.get_neighbors(E))[0])

    assert_production_cannot_be_applied(P3, G)


def test_P3_left_side_wrong_label():
    # test application of P3 to the graph isomorphic to left side of P3 with not appropiate label
    G = make_initial_graph_P3()
    E = G.get_first_node_with_label('E')
    G.replace_node(E, Node(label='e', x=E.x, y=E.y, level=E.level))

    assert_production_cannot_be_applied(P3, G)


def test_P3_left_side_subgraph():
    # test application of P3 to the graph with the subgraph isomorphic to left side of P3
    G = make_initial_graph_P3()
    expected = make_right_side_graph_P3()

    def add_node(G: Graph) -> None:
        X = Node(label='E', x=-.5, y=-.5, level=1)
        Es = G.get_duplicates_of(X)
        E = Es[0]
        S = Node(label='S', x=-1, y=-1, level=2)
        G.add_node(S)
        G.add_edge(E, S)

    add_node(G)
    add_node(expected)

    P3(G)

    assert G.is_isomorphic_with(expected)


def test_P3_left_side_invariance():
    # test invariance of the left side graph when production cannot be applied
    G = make_initial_graph_P3()
    expected = make_initial_graph_P3()

    def remove_node(G: Graph) -> None:
        E = G.get_first_node_with_label('E')
        G.remove_node(E)

    remove_node(G)
    remove_node(expected)

    assert_production_cannot_be_applied(P3, G)
    assert G.is_isomorphic_with(expected)


def test_P4_isomorphic_left_side():
    # test application of P4 to the graph isomorphic to left side of P4
    G = make_initial_graph_P4()
    expected = make_right_side_graph_P4()

    P4(G)

    assert G.is_isomorphic_with(expected)


def test_P4_left_side_deleted_node():
    # test application of P4 to the graph isomorphic to left side of P4 with deleted one node
    G = make_initial_graph_P4()
    E = G.get_first_node_with_label('E')
    G.remove_node(E)

    assert_production_cannot_be_applied(P4, G)


def test_P4_left_side_deleted_edge():
    # test application of P4 to the graph isomorphic to left side of P4 with deleted one edge
    G = make_initial_graph_P4()
    E = G.get_first_node_with_label('E')
    G.remove_edge(E, list(G.get_neighbors(E))[0])

    assert_production_cannot_be_applied(P4, G)


def test_P4_left_side_wrong_label():
    # test application of P4 to the graph isomorphic to left side of P4 with not appropiate label
    G = make_initial_graph_P4()
    E = G.get_first_node_with_label('E')
    G.replace_node(E, Node(label='e', x=E.x, y=E.y, level=E.level))

    assert_production_cannot_be_applied(P4, G)


def test_P4_left_side_subgraph():
    # test application of P4 to the graph with the subgraph isomorphic to left side of P4
    G = make_initial_graph_P4()
    expected = make_right_side_graph_P4()

    def add_node(G: Graph) -> None:
        X = Node(label='E', x=-.5, y=-.5, level=1)
        Es = G.get_duplicates_of(X)
        E = Es[0]
        S = Node(label='S', x=-1, y=-1, level=2)
        G.add_node(S)
        G.add_edge(E, S)

    add_node(G)
    add_node(expected)

    P4(G)

    assert G.is_isomorphic_with(expected)


def test_P4_left_side_invariance():
    # test invariance of the left side graph when production cannot be applied
    G = make_initial_graph_P4()
    expected = make_initial_graph_P4()

    def remove_node(G: Graph) -> None:
        E = G.get_first_node_with_label('E')
        G.remove_node(E)

    remove_node(G)
    remove_node(expected)

    assert_production_cannot_be_applied(P4, G)
    assert G.is_isomorphic_with(expected)
