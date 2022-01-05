from GramatykiGrafoweAGH import Graph, Node
from GramatykiGrafoweAGH.project.task4 import P7
from GramatykiGrafoweAGH.testing import assert_production_cannot_be_applied


def make_P7_left_side_graph():
    G = Graph()

    level = 2

    E = Node(label='E', x=0, y=0, level=level)
    iL = Node(label='i', x=-1, y=-1, level=level)
    iR = Node(label='i', x=1, y=-1, level=level)

    I1L = Node(label='I', x=-2, y=-2, level=level + 1)
    I2L = Node(label='I', x=-1, y=-2, level=level + 1)

    I1R = Node(label='I', x=1, y=-2, level=level + 1)
    I2R = Node(label='I', x=2, y=-2, level=level + 1)

    E1L = Node(label='E', x=0, y=-3, level=level + 1)
    E2L = Node(label='E', x=0, y=-4, level=level + 1)
    E3L = Node(label='E', x=0, y=-5, level=level + 1)

    E1R = Node(label='E', x=0, y=-3, level=level + 1)
    E2R = Node(label='E', x=0, y=-4, level=level + 1)
    E3R = Node(label='E', x=0, y=-5, level=level + 1)

    G.add_nodes([E, iL, iR, I1L, I2L, I1R, I2R, E1L, E2L, E3L, E1R, E2R, E3R])

    G.add_edges([
        (E, iL), (E, iR), (iL, I1L), (iL, I2L), (iR, I1R), (iR, I2R),
        (I1L, E1L), (I1L, E2L), (I2L, E2L), (I2L, E3L),
        (I1R, E1R), (I1R, E2R), (I2R, E2R), (I2R, E3R),
        (E1L, E2L), (E2L, E3L), (E1R, E2R), (E2R, E3R)
    ])

    return G


def make_P7_left_side_graph_not_middle():
    G = make_P7_left_side_graph()

    E1, E2 = G.get_nodes_with_predicate(lambda n: n.label == 'E' and n.level == 3 and n.y == -4)
    E1a = Node(label=E1.label, x=E1.x, y=E1.y + 0.2, level=E1.level)
    E2a = Node(label=E2.label, x=E2.x, y=E2.y + 0.2, level=E2.level)

    G.replace_node(E1, E1a)
    G.replace_node(E2, E2a)

    return G


def make_P7_right_side_graph():
    G = Graph()

    level = 2

    E = Node(label='E', x=0, y=0, level=level)
    iL = Node(label='i', x=-1, y=-1, level=level)
    iR = Node(label='i', x=1, y=-1, level=level)

    I1L = Node(label='I', x=-2, y=-2, level=level + 1)
    I2L = Node(label='I', x=-1, y=-2, level=level + 1)

    I1R = Node(label='I', x=1, y=-2, level=level + 1)
    I2R = Node(label='I', x=2, y=-2, level=level + 1)

    E1 = Node(label='E', x=0, y=-3, level=level + 1)
    E2 = Node(label='E', x=0, y=-4, level=level + 1)
    E3 = Node(label='E', x=0, y=-5, level=level + 1)

    G.add_nodes([E, iL, iR, I1L, I2L, I1R, I2R, E1, E2, E3])

    G.add_edges([
        (E, iL), (E, iR), (iL, I1L), (iL, I2L), (iR, I1R), (iR, I2R),
        (I1L, E1), (I1L, E2), (I2L, E2), (I2L, E3),
        (I1R, E1), (I1R, E2), (I2R, E2), (I2R, E3),
        (E1, E2), (E2, E3)
    ])

    return G


def test_P7_isomorphic_left_side():
    G = make_P7_left_side_graph()

    P7(G)

    assert G.number_of_nodes == 10

    assert G.number_of_edges == 16

    Es = G.get_nodes_with_predicate(lambda n: n.level == 3 and n.label == 'E')

    assert len(Es) == 3

    G.is_isomorphic_with(make_P7_right_side_graph())


def test_P7_can_be_applied_only_once():
    G = make_P7_left_side_graph()

    P7(G)

    assert_production_cannot_be_applied(P7, G)


def test_P7_left_side_deleted_node():
    G = make_P7_left_side_graph()

    I = G.get_first_node_with_label('I')
    G.remove_node(I)

    assert_production_cannot_be_applied(P7, G)


def test_P7_left_side_deleted_edge():
    G = make_P7_left_side_graph()

    I = G.get_first_node_with_label('I')
    G.remove_edge(I, next(G.get_neighbors(I)))

    assert_production_cannot_be_applied(P7, G)


def test_P7_left_side_wrong_label():
    G = make_P7_left_side_graph()

    I = G.get_first_node_with_label('I')
    G.replace_node(I, Node(label='e', x=I.x, y=I.y, level=I.level))

    assert_production_cannot_be_applied(P7, G)


def test_P7_left_side_subgraph():
    # test application of P7 to the graph with the subgraph isomorphic to left side of P7
    G = make_P7_left_side_graph()
    expected = make_P7_right_side_graph()

    def add_node(G: Graph) -> None:
        E = G.get_first_node_with_label('E')
        E1 = Node(label='E', x=-1, y=-1, level=2)
        G.add_node(E1)
        G.add_edge(E, E1)

    add_node(G)
    add_node(expected)

    P7(G)

    assert G.is_isomorphic_with(expected)


def test_P7_left_side_invariance():
    # test invariance of the left side graph when production cannot be applied
    G = make_P7_left_side_graph()
    expected = make_P7_left_side_graph()

    def modify_graph(graph):
        I = graph.get_first_node_with_label('I')
        graph.remove_node(I)

    modify_graph(G)
    modify_graph(expected)

    assert_production_cannot_be_applied(P7, G)
    assert G.is_isomorphic_with(expected)


def test_P7_on_P8_graph():
    G = make_P7_left_side_graph()

    E1L, E1R = G.get_nodes_with_predicate(lambda n: n.label == "E" and n.x == 0 and n.y == -3 and n.level == 3)
    G.merge_two_nodes(E1L, E1R)

    assert_production_cannot_be_applied(P7, G)


def test_P7_left_side_not_middle():
    G = make_P7_left_side_graph_not_middle()
    assert_production_cannot_be_applied(P7, G)
