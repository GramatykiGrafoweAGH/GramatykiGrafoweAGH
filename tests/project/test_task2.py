from GramatykiGrafoweAGH import Graph, Node
from GramatykiGrafoweAGH.project.task2 import P3, P4
from GramatykiGrafoweAGH.testing import assert_production_cannot_be_applied


def make_initial_graph_P3() -> Graph:
    G = Graph()

    I = Node(label='I', x=0, y=0, level=1)
    E00 = Node(label='E', x=-.5, y=-.5, level=1)
    E20 = Node(label='E', x=-.5, y=.5, level=1)
    E02 = Node(label='E', x=.5, y=-.5, level=1)
    E22 = Node(label='E', x=.5, y=.5, level=1)
    E10 = Node(label='E', x=-.5, y=0, level=1)

    G.add_nodes([I, E00, E02, E20, E22, E10])

    G.add_edges([
        (I, E20), (I, E22), (I, E00), (I, E02),
        (E00, E02),
        (E00, E10), (E10, E20),
        (E20, E22),
        (E22, E02),
    ])

    return G


def make_initial_graph_P4() -> Graph:
    G = Graph()

    I = Node(label='I', x=0, y=0, level=1)
    E00 = Node(label='E', x=-.5, y=-.5, level=1)
    E20 = Node(label='E', x=-.5, y=.5, level=1)
    E02 = Node(label='E', x=.5, y=-.5, level=1)
    E22 = Node(label='E', x=.5, y=.5, level=1)
    E10 = Node(label='E', x=-.5, y=0, level=1)
    E21 = Node(label='E', x=0, y=.5, level=1)

    G.add_nodes([I, E00, E02, E20, E22, E21, E10])

    G.add_edges([
        (I, E00), (I, E02), (I, E20), (I, E22),
        (E00, E02),
        (E00, E10), (E10, E20),
        (E02, E22),
        (E20, E21), (E21, E22),
    ])

    return G


def make_right_side_graph_P3():
    G = Graph()

    level = 1

    x00, y00 = -0.5, -0.5
    x01, y01 = 0.0, -0.5
    x02, y02 = 0.5, -0.5
    x10, y10 = -0.5, 0.0
    x11, y11 = 0.0, 0.0
    x12, y12 = 0.5, 0.0
    x20, y20 = -0.5, 0.5
    x21, y21 = 0.0, 0.5
    x22, y22 = 0.5, 0.5

    i = Node(label='i', x=x11, y=y11, level=level)
    E00 = Node(label='E', x=x00, y=y00, level=level)
    E02 = Node(label='E', x=x02, y=y02, level=level)
    E20 = Node(label='E', x=x20, y=y20, level=level)
    E22 = Node(label='E', x=x22, y=y22, level=level)

    E10 = Node(label='E', x=x10, y=y10, level=level)

    G.add_nodes([i, E00, E02, E20, E22, E10])

    G.add_edges([
        (i, E00), (i, E02), (i, E20), (i, E22),
        (E00, E02),
        (E00, E10), (E10, E20),
        (E02, E22),
        (E20, E22),
    ])

    I00 = Node(label='I', x=(x00 + x11) / 2, y=(y00 + y11) / 2, level=level + 1)
    I01 = Node(label='I', x=(x02 + x11) / 2, y=(y02 + y11) / 2, level=level + 1)
    I10 = Node(label='I', x=(x20 + x11) / 2, y=(y20 + y11) / 2, level=level + 1)
    I11 = Node(label='I', x=(x22 + x11) / 2, y=(y22 + y11) / 2, level=level + 1)

    E00 = Node(label='E', x=x00, y=y00, level=level + 1)
    E01 = Node(label='E', x=x01, y=y01, level=level + 1)
    E02 = Node(label='E', x=x02, y=y02, level=level + 1)
    E10 = Node(label='E', x=x10, y=y10, level=level + 1)
    E11 = Node(label='E', x=x11, y=y11, level=level + 1)
    E12 = Node(label='E', x=x12, y=y12, level=level + 1)
    E20 = Node(label='E', x=x20, y=y20, level=level + 1)
    E21 = Node(label='E', x=x21, y=y21, level=level + 1)
    E22 = Node(label='E', x=x22, y=y22, level=level + 1)

    G.add_nodes([
        I00, I01, I10, I11,
        E00, E01, E02,
        E10, E11, E12,
        E20, E21, E22,
    ])

    G.add_edges([
        (i, I00), (i, I01), (i, I10), (i, I11),
        (I00, E00), (I00, E01), (I00, E10), (I00, E11),
        (I01, E01), (I01, E02), (I01, E11), (I01, E12),
        (I10, E10), (I10, E11), (I10, E20), (I10, E21),
        (I11, E11), (I11, E12), (I11, E21), (I11, E22),

        (E00, E01), (E01, E02),
        (E10, E11), (E11, E12),
        (E20, E21), (E21, E22),

        (E00, E10), (E10, E20),
        (E01, E11), (E11, E21),
        (E02, E12), (E12, E22),
    ])

    return G


def make_right_side_graph_P4():
    G = Graph()

    level = 1

    x00, y00 = -0.5, -0.5
    x01, y01 = 0.0, -0.5
    x02, y02 = 0.5, -0.5
    x10, y10 = -0.5, 0.0
    x11, y11 = 0.0, 0.0
    x12, y12 = 0.5, 0.0
    x20, y20 = -0.5, 0.5
    x21, y21 = 0.0, 0.5
    x22, y22 = 0.5, 0.5

    i = Node(label='i', x=x11, y=y11, level=level)
    E00 = Node(label='E', x=x00, y=y00, level=level)
    E02 = Node(label='E', x=x02, y=y02, level=level)
    E20 = Node(label='E', x=x20, y=y20, level=level)
    E22 = Node(label='E', x=x22, y=y22, level=level)

    E10 = Node(label='E', x=x10, y=y10, level=level)
    E21 = Node(label='E', x=x21, y=y21, level=level)

    G.add_nodes([i, E00, E02, E20, E22, E10, E21])

    G.add_edges([
        (i, E00), (i, E02), (i, E20), (i, E22),
        (E00, E02),
        (E00, E10), (E10, E20),
        (E02, E22),
        (E20, E21), (E21, E22),
    ])

    I00 = Node(label='I', x=(x00 + x11) / 2, y=(y00 + y11) / 2, level=level + 1)
    I01 = Node(label='I', x=(x02 + x11) / 2, y=(y02 + y11) / 2, level=level + 1)
    I10 = Node(label='I', x=(x20 + x11) / 2, y=(y20 + y11) / 2, level=level + 1)
    I11 = Node(label='I', x=(x22 + x11) / 2, y=(y22 + y11) / 2, level=level + 1)

    E00 = Node(label='E', x=x00, y=y00, level=level + 1)
    E01 = Node(label='E', x=x01, y=y01, level=level + 1)
    E02 = Node(label='E', x=x02, y=y02, level=level + 1)
    E10 = Node(label='E', x=x10, y=y10, level=level + 1)
    E11 = Node(label='E', x=x11, y=y11, level=level + 1)
    E12 = Node(label='E', x=x12, y=y12, level=level + 1)
    E20 = Node(label='E', x=x20, y=y20, level=level + 1)
    E21 = Node(label='E', x=x21, y=y21, level=level + 1)
    E22 = Node(label='E', x=x22, y=y22, level=level + 1)

    G.add_nodes([
        I00, I01, I10, I11,
        E00, E01, E02,
        E10, E11, E12,
        E20, E21, E22,
    ])

    G.add_edges([
        (i, I00), (i, I01), (i, I10), (i, I11),
        (I00, E00), (I00, E01), (I00, E10), (I00, E11),
        (I01, E01), (I01, E02), (I01, E11), (I01, E12),
        (I10, E10), (I10, E11), (I10, E20), (I10, E21),
        (I11, E11), (I11, E12), (I11, E21), (I11, E22),

        (E00, E01), (E01, E02),
        (E10, E11), (E11, E12),
        (E20, E21), (E21, E22),

        (E00, E10), (E10, E20),
        (E01, E11), (E11, E21),
        (E02, E12), (E12, E22),
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
