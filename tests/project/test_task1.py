from GramatykiGrafoweAGH.project.task1 import make_initial_graph, P2
from GramatykiGrafoweAGH.testing import assert_production_cannot_be_applied
from GramatykiGrafoweAGH import Node, Graph


def make_P2_left_side_graph():
    G = Graph()

    x0, y0 = 0, 0
    level = 1

    x1, y1 = -0.5, -0.5
    x2, y2 = 0.5, -0.5
    x3, y3 = -0.5, 0.5
    x4, y4 = 0.5, 0.5

    I = Node(label='I', x=x0, y=y0, level=level + 1)
    E1 = Node(label='E', x=x1, y=y1, level=level + 1)
    E2 = Node(label='E', x=x2, y=y2, level=level + 1)
    E3 = Node(label='E', x=x3, y=y3, level=level + 1)
    E4 = Node(label='E', x=x4, y=y4, level=level + 1)

    G.add_nodes([I, E1, E2, E3, E4])

    G.add_edges([
        (I, E1), (I, E2), (I, E3), (I, E4),
        (E1, E2), (E2, E4), (E4, E3), (E3, E1),
    ])

    return G


def make_P2_right_side_graph():
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

    i = Node(label='i', x=x0, y=y0, level=level + 1)
    E1 = Node(label='E', x=x1, y=y1, level=level + 1)
    E2 = Node(label='E', x=x2, y=y2, level=level + 1)
    E3 = Node(label='E', x=x3, y=y3, level=level + 1)
    E4 = Node(label='E', x=x4, y=y4, level=level + 1)

    G.add_nodes([i, E1, E2, E3, E4])

    G.add_edges([
        (i, E1), (i, E2), (i, E3), (i, E4),
        (E1, E2), (E2, E4), (E4, E3), (E3, E1),
    ])

    I1 = Node(label='I', x=(x1 + x9) / 2, y=(y1 + y9) / 2, level=level + 2)
    I2 = Node(label='I', x=(x2 + x9) / 2, y=(y2 + y9) / 2, level=level + 2)
    I3 = Node(label='I', x=(x3 + x9) / 2, y=(y3 + y9) / 2, level=level + 2)
    I4 = Node(label='I', x=(x4 + x9) / 2, y=(y4 + y9) / 2, level=level + 2)

    E1 = Node(label='E', x=x1, y=y1, level=level + 2)
    E2 = Node(label='E', x=x2, y=y2, level=level + 2)
    E3 = Node(label='E', x=x3, y=y3, level=level + 2)
    E4 = Node(label='E', x=x4, y=y4, level=level + 2)
    E5 = Node(label='E', x=x5, y=y5, level=level + 2)
    E6 = Node(label='E', x=x6, y=y6, level=level + 2)
    E7 = Node(label='E', x=x7, y=y7, level=level + 2)
    E8 = Node(label='E', x=x8, y=y8, level=level + 2)
    E9 = Node(label='E', x=x9, y=y9, level=level + 2)

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


def test_make_initial_graph():
    G = make_initial_graph()

    assert G.number_of_nodes == 1
    assert G.number_of_edges == 0

    node, = G.nodes

    assert node.label == 'E'
    assert node.x == 0.5
    assert node.y == 0.5
    assert node.level == 0


def test_P1():
    pass


def test_P2_isomorphic_left_side():
    # test application of P2 to the graph isomorphic to left side of P2
    G = make_P2_left_side_graph()
    G2 = make_P2_right_side_graph()

    P2(G)
    assert G.is_isomorphic_with(G2)


def test_P2_left_side_deleted_node():
    # test application of P2 to the graph isomorphic to left side of P2 with deleted one node
    G = make_P2_left_side_graph()

    u = G.get_first_node_with_label('E')
    G.remove_node(u)

    assert_production_cannot_be_applied(P2, G)


def test_P2_left_side_deleted_edge():
    # test application of P2 to the graph isomorphic to left side of P2 with deleted one edge
    G = make_P2_left_side_graph()
    u = G.get_first_node_with_label('E')
    G.remove_edge(u, list(G.neighbors(u))[0])

    assert_production_cannot_be_applied(P2, G)


def test_P2_left_side_wrong_level():
    # test application of P2 to the graph isomorphic to left side of P2 with not appropiate label
    G = make_P2_left_side_graph()
    u = G.get_first_node_with_label('E')
    G.replace_node(u, Node(label='H', x=u.x, y=u.y, level=u.level))

    assert_production_cannot_be_applied(P2, G)


def test_P2_left_side_wrong_coordinates():
    # test application of P2 to the graph isomorphic to left side of P2 with not appropiate coordinates
    G = make_P2_left_side_graph()
    u = G.get_first_node_with_label('E')
    G.replace_node(u, Node(label='H', x=u.x, y=u.y + 0.9, level=u.level))

    assert_production_cannot_be_applied(P2, G)


def test_P2_left_side_subgraph():
    # test application of P2 to the graph with the subgraph isomorphic to left side of P2
    G = make_P2_left_side_graph()
    G2 = make_P2_right_side_graph()
    u = Node(label='S', x=-1, y=-1, level=2)
    G.add_node(u)
    v = G.get_first_node_with_label('E')
    G.add_edge(u, v)

    G2.add_node(u)
    v = G2.get_first_node_with_label('E')
    G2.add_edge(u, v)

    P2(G)
    assert G.is_isomorphic_with(G2)


def test_P2_left_side_invariance():
    # test invariance of the left side graph when production cannot be applied
    G = make_P2_left_side_graph()
    G2 = make_P2_left_side_graph()

    u = G.get_first_node_with_label('E')
    G.remove_node(u)

    u2 = G2.get_first_node_with_label('E')
    G2.remove_node(u2)

    assert_production_cannot_be_applied(P2, G)
    assert G.is_isomorphic_with(G2)
