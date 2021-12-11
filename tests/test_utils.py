import networkx as nx

from GramatykiGrafoweAGH import Node
from GramatykiGrafoweAGH.utils import replace_node, merge_two_nodes


def test_replace_node():
    G = nx.Graph()
    A = Node(label='A', x=1, y=1, level=0)
    B = Node(label='B', x=2, y=2, level=0)
    C = Node(label='C', x=3, y=3, level=0)

    G.add_nodes_from([A, B, C])

    G.add_edges_from([(A, B), (B, C)])

    D = Node(label='D', x=4, y=4, level=0)

    replace_node(G, B, D)

    assert G.number_of_nodes() == 3
    assert G.number_of_edges() == 2

    assert B not in G
    assert D in G

    assert set(G.neighbors(A)) == {D}
    assert set(G.neighbors(C)) == {D}
    assert set(G.neighbors(D)) == {A, C}


def test_merge_two_nodes():
    G = nx.Graph()

    A = Node(label='A', x=1, y=1, level=0)
    B1 = Node(label='B', x=2, y=2, level=0)
    B2 = Node(label='B', x=2, y=2, level=0)
    C = Node(label='C', x=3, y=3, level=0)

    G.add_nodes_from([A, B1, B2, C])

    G.add_edges_from([(A, B1), (B2, C)])

    B = merge_two_nodes(G, B1, B2)

    assert G.number_of_nodes() == 3
    assert G.number_of_edges() == 2

    assert B1 not in G
    assert B2 not in G
    assert B in G

    assert set(G.neighbors(A)) == {B}
    assert set(G.neighbors(C)) == {B}
    assert set(G.neighbors(B)) == {A, C}
