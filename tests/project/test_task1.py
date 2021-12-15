from GramatykiGrafoweAGH.project.task1 import P2
from GramatykiGrafoweAGH.project.utils import is_node_between
from GramatykiGrafoweAGH.testing import assert_production_cannot_be_applied
import pytest
from typing import List

from GramatykiGrafoweAGH import Graph, Node, CannotApplyProductionError
from GramatykiGrafoweAGH.project.task1 import make_initial_graph, P1

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


def check_if_production_applied(G: Graph, e: Node):
    Is = list(filter(lambda n: n.level == 1 and n.label == "I", G.neighbors(e)))

    assert len(Is) == 1
    I = Is[0]

    Es = list(filter(lambda n: n.level == 1, G.neighbors(I)))
    assert len(Es) == 4

    check_square(G, Es, I)


def check_square(G: Graph, Es: List[Node], I: Node):
    for E in Es:
        assert E in G.neighbors(I)

    level_0 = list(filter(lambda n: n.level == 0 and n.label == "e", G.nodes))
    assert len(level_0) == 1

    for E in Es:
        for neighbour in G.neighbors(E):
            if neighbour.label == "E":
                assert neighbour in Es
                assert bool(neighbour.x == E.x) != bool(neighbour.y == E.y)
            else:
                assert neighbour.label == "I"
                E_not_neighbours = [E1 for E1 in Es if E1 not in G.neighbors(E) and E1 != E]
                assert len(E_not_neighbours) == 1
                assert is_node_between(E_not_neighbours[0], neighbour, E)


def test_P1_isomorphic():
    G = Graph()
    original_E = Node(label='E', x=0.5, y=0.5, level=0)
    G.add_node(original_E)

    P1(G)

    assert len(G.nodes) == 6

    level_0 = list(filter(lambda n: n.level == 0, G.nodes))
    assert len(level_0) == 1
    e = level_0[0]
    assert e.label == "e"

    level_1 = list(filter(lambda n: n.level == 1, G.nodes))
    assert len(level_1) == 5

    Es = [n for n in level_1 if n.label == "E"]
    Is = [n for n in level_1 if n.label == "I"]

    assert len(Es) == 4
    assert len(Is) == 1

    I: Node = Is[0]

    check_square(G, Es, I)


def test_P1_vertex_removed():
    """Empty graph"""
    G = Graph()

    assert G.number_of_nodes == 0

    assert_production_cannot_be_applied(P1, G)


def test_P1_edge_removed():
    """Inapplicable"""
    pass


def test_P1_label_changed():
    """small letter e"""
    G = Graph()
    e = Node(label='e', x=0.5, y=0.5, level=0)
    G.add_node(e)

    assert_production_cannot_be_applied(P1, G)


def test_P1_subgraph():
    G = Graph()
    E = Node(label='E', x=0.5, y=0.5, level=0)
    i0 = Node(label='i', x=2.0, y=2.0, level=0)
    i1 = Node(label='i', x=-1.0, y=-1.0, level=0)

    G.add_node(E)
    G.add_node(i0)
    G.add_node(i1)

    G.add_edges([(i0, E), (E, i1)])
    P1(G)

    assert len(G.nodes) == 8

    level_0 = list(filter(lambda n: n.level == 0, G.nodes))
    assert len(level_0) == 3

    es = list(filter(lambda n: n.label == "e", level_0))
    assert len(es) == 1
    e = es[0]

    check_if_production_applied(G, e)


def test_P1_subgraph_dont_apply():
    def make_graph() -> Graph:
        G = Graph()
        I = Node(label='I', x=0.5, y=0.5, level=0)
        i0 = Node(label='i', x=2.0, y=2.0, level=0)
        i1 = Node(label='i', x=-1.0, y=-1.0, level=0)

        G.add_node(I)
        G.add_node(i0)
        G.add_node(i1)

        G.add_edges([(i0, I), (I, i1)])
        return G

    G = make_graph()
    nodes = G.nodes

    assert_production_cannot_be_applied(P1, G)

    G1 = make_graph()

    assert G.number_of_nodes == G1.number_of_nodes
    assert G.number_of_edges == G1.number_of_edges

    assert nodes == G.nodes


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
