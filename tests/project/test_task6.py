from GramatykiGrafoweAGH import Graph, Node
from GramatykiGrafoweAGH.project.task6 import P9
from GramatykiGrafoweAGH.testing import assert_production_cannot_be_applied
from test_task4 import make_P7_left_side_graph

def make_P9_left_side_graph():
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
    E3 = Node(label='E', x=2, y=2, level=level + 1)
    
    E2L = Node(label='E', x=1, y=1, level=level + 1)
    
    E2R = Node(label='E', x=1, y=1, level=level + 1)

    G.add_nodes([E, iL, iR, I1L, I2L, I1R, I2R, E1, E2L, E2R, E3])

    G.add_edges([
        (E, iL), (E, iR), (iL, I1L), (iL, I2L), (iR, I1R), (iR, I2R),
        (I1L, E1), (I1L, E2L), (I2L, E2L), (I2L, E3),
        (I1R, E1), (I1R, E2R), (I2R, E2R), (I2R, E3),
        (E1, E2L), (E2L, E3), (E1, E2R), (E2R, E3)
    ])

    return G

def make_P9_right_side_graph():
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


def test_P9_isomorphic_left_side():
    G = make_P9_left_side_graph()

    P9(G)

    assert len(G.nodes) == 10

    assert G.number_of_edges == 16

    Es = list(filter(lambda n: n.level == 3 and n.label == 'E', G.nodes))

    assert len(Es) == 3

    G.is_isomorphic_with(make_P9_right_side_graph())


def test_P9_can_be_applied_only_once():
    G = make_P9_left_side_graph()

    P9(G)

    assert_production_cannot_be_applied(P9, G)


def test_P9_left_side_deleted_node():
    G = make_P9_left_side_graph()

    I = G.get_first_node_with_label('I')
    G.remove_node(I)

    assert_production_cannot_be_applied(P9, G)


def test_P9_left_side_deleted_edge():
    G = make_P9_left_side_graph()

    I = G.get_first_node_with_label('I')
    G.remove_edge(I, list(G.get_neighbors(I))[0])

    assert_production_cannot_be_applied(P9, G)


def test_P9_left_side_wrong_label():
    G = make_P9_left_side_graph()

    I = G.get_first_node_with_label('I')
    G.replace_node(I, Node(label='e', x=I.x, y=I.y, level=I.level))

    assert_production_cannot_be_applied(P9, G)


def test_P9_left_side_subgraph():
    # test application of P9 to the graph with the subgraph isomorphic to left side of P9
    G = make_P9_left_side_graph()
    expected = make_P9_right_side_graph()

    def add_node(G: Graph) -> None:
        E = G.get_first_node_with_label('E')
        E1 = Node(label='E', x=-1, y=-1, level=2)
        G.add_node(E1)
        G.add_edge(E, E1)

    add_node(G)
    add_node(expected)

    P9(G)

    assert G.is_isomorphic_with(expected)


def test_P9_left_side_invariance():
    # test invariance of the left side graph when production cannot be applied
    G = make_P9_left_side_graph()
    expected = make_P9_left_side_graph()

    I = G.get_first_node_with_label('I')
    G.remove_node(I)

    I = expected.get_first_node_with_label('I')
    expected.remove_node(I)

    assert_production_cannot_be_applied(P9, G)
    assert G.is_isomorphic_with(expected)


def test_P9_on_P7_graph():
    G = make_P7_left_side_graph()

    assert_production_cannot_be_applied(P9, G)
