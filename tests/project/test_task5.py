from GramatykiGrafoweAGH import Graph, Node
from GramatykiGrafoweAGH.project.task5 import P8
from GramatykiGrafoweAGH.testing import assert_production_cannot_be_applied


def make_P8_left_side_graph():
    G = Graph()

    level = 2

    E = Node(label='E', x=0, y=0, level=level)
    iL = Node(label='i', x=0, y=0, level=level)
    iR = Node(label='i', x=0, y=0, level=level)

    I1L = Node(label='I', x=0, y=0, level=level + 1)
    I2L = Node(label='I', x=0, y=0, level=level + 1)

    I1R = Node(label='I', x=0, y=0, level=level + 1)
    I2R = Node(label='I', x=0, y=0, level=level + 1)

    E1 = Node(label='E', x=0, y=0, level=level + 1)

    E2L = Node(label='E', x=1, y=1, level=level + 1)
    E3L = Node(label='E', x=2, y=2, level=level + 1)

    E2R = Node(label='E', x=1, y=1, level=level + 1)
    E3R = Node(label='E', x=2, y=2, level=level + 1)

    G.add_nodes([E, iL, iR, I1L, I2L, I1R, I2R, E1, E2L, E3L, E2R, E3R])

    G.add_edges([
        (E, iL), (E, iR), (iL, I1L), (iL, I2L), (iR, I1R), (iR, I2R),
        (I1L, E1), (I1L, E2L), (I2L, E2L), (I2L, E3L),
        (I1R, E1), (I1R, E2R), (I2R, E2R), (I2R, E3R),
        (E1, E2L), (E2L, E3L), (E1, E2R), (E2R, E3R)
    ])

    return G


def make_P8_right_side_graph():
    G = Graph()

    level = 2

    E = Node(label='E', x=0, y=0, level=level)
    iL = Node(label='i', x=0, y=0, level=level)
    iR = Node(label='i', x=0, y=0, level=level)

    I1L = Node(label='I', x=0, y=0, level=level + 1)
    I2L = Node(label='I', x=0, y=0, level=level + 1)

    I1R = Node(label='I', x=0, y=0, level=level + 1)
    I2R = Node(label='I', x=0, y=0, level=level + 1)

    E1 = Node(label='E', x=0, y=0, level=level + 1)
    E2 = Node(label='E', x=1, y=1, level=level + 1)
    E3 = Node(label='E', x=2, y=2, level=level + 1)

    G.add_nodes([E, iL, iR, I1L, I2L, I1R, I2R, E1, E2, E3])

    G.add_edges([
        (E, iL), (E, iR), (iL, I1L), (iL, I2L), (iR, I1R), (iR, I2R),
        (I1L, E1), (I1L, E2), (I2L, E2), (I2L, E3),
        (I1R, E1), (I1R, E2), (I2R, E2), (I2R, E3),
        (E1, E2), (E2, E3)
    ])

    return G


def test_P8_isomorphic_left_side():
    G = make_P8_left_side_graph()

    P8(G)

    assert G.number_of_nodes == 10

    assert G.number_of_edges == 16

    Es = G.get_nodes_with_predicate(lambda n: n.level == 3 and n.label == 'E')

    assert len(Es) == 3

    G.is_isomorphic_with(make_P8_right_side_graph())


def test_P8_can_be_applied_only_once():
    G = make_P8_left_side_graph()

    P8(G)

    assert_production_cannot_be_applied(P8, G)


def test_P8_left_side_deleted_node():
    G = make_P8_left_side_graph()

    I = G.get_first_node_with_label('I')
    G.remove_node(I)

    assert_production_cannot_be_applied(P8, G)


def test_P8_left_side_deleted_edge():
    G = make_P8_left_side_graph()

    I = G.get_first_node_with_label('I')
    G.remove_edge(I, next(G.get_neighbors(I)))

    assert_production_cannot_be_applied(P8, G)


def test_P8_left_side_wrong_label():
    G = make_P8_left_side_graph()

    I = G.get_first_node_with_label('I')
    G.replace_node(I, Node(label='e', x=I.x, y=I.y, level=I.level))

    assert_production_cannot_be_applied(P8, G)


def test_P8_left_side_subgraph():
    # test application of P8 to the graph with the subgraph isomorphic to left side of P8
    G = make_P8_left_side_graph()
    expected = make_P8_right_side_graph()

    def add_node(G: Graph) -> None:
        E = G.get_first_node_with_label('E')
        E1 = Node(label='E', x=-1, y=-1, level=2)
        G.add_node(E1)
        G.add_edge(E, E1)

    add_node(G)
    add_node(expected)

    P8(G)

    assert G.is_isomorphic_with(expected)


def test_P8_left_side_invariance():
    # test invariance of the left side graph when production cannot be applied
    G = make_P8_left_side_graph()
    expected = make_P8_left_side_graph()

    def modify_graph(graph):
        I = graph.get_first_node_with_label('I')
        graph.remove_node(I)

    modify_graph(G)
    modify_graph(expected)

    assert_production_cannot_be_applied(P8, G)
    assert G.is_isomorphic_with(expected)


def test_P8_on_P9_graph():
    G = make_P8_left_side_graph()

    E3L, E3R = G.get_nodes_with_predicate(lambda n: n.label == "E" and n.x == 2 and n.level == 3)
    G.merge_two_nodes(E3L, E3R)

    assert_production_cannot_be_applied(P8, G)
