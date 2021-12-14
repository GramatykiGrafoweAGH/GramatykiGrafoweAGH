import pytest
from typing import List

from GramatykiGrafoweAGH import Graph, Node, CannotApplyProductionError
from GramatykiGrafoweAGH.project.task1 import make_initial_graph, P1


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


def check_square(G: Graph, Es: List[Node], I: Node):
    for E in Es:
        assert E in G.neighbors(I)

    level_0 = list(filter(lambda n: n.level == 0, G.nodes))
    assert len(level_0) == 1
    e = level_0[0]
    assert e.label == "e"

    for E in Es:
        for neighbour in G.neighbors(E):
            if neighbour.label == "E":
                assert neighbour in Es
                assert bool(neighbour.x == E.x) != bool(neighbour.y == E.y)
            else:
                assert neighbour.label == "I"
                E_not_neighbours = [E1 for E1 in Es if E1 not in G.neighbors(E) and E1 != E]
                assert len(E_not_neighbours) == 1
                E_not_neighbour = E_not_neighbours[0]
                assert (E_not_neighbour.x + E.x) / 2 == neighbour.x
                assert (E_not_neighbour.y + E.y) / 2 == neighbour.y


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

    with pytest.raises(CannotApplyProductionError):
        P1(G)


def test_P2():
    pass
