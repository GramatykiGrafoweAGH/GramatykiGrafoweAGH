from GramatykiGrafoweAGH import Node, Graph


def test_replace_node():
    G = Graph()

    A = Node(label='A', x=1, y=1, level=0)
    B = Node(label='B', x=2, y=2, level=0)
    C = Node(label='C', x=3, y=3, level=0)

    G.add_nodes([A, B, C])

    G.add_edges([(A, B), (B, C)])

    D = Node(label='D', x=4, y=4, level=0)

    G.replace_node(B, D)

    assert G.number_of_nodes == 3
    assert G.number_of_edges == 2

    assert B not in G
    assert D in G

    assert set(G.neighbors(A)) == {D}
    assert set(G.neighbors(C)) == {D}
    assert set(G.neighbors(D)) == {A, C}


def test_merge_two_nodes():
    G = Graph()

    A = Node(label='A', x=1, y=1, level=0)
    B1 = Node(label='B', x=2, y=2, level=0)
    B2 = Node(label='B', x=2, y=2, level=0)
    C = Node(label='C', x=3, y=3, level=0)

    G.add_nodes([A, B1, B2, C])

    G.add_edges([(A, B1), (B2, C)])

    B = G.merge_two_nodes(B1, B2)

    assert G.number_of_nodes == 3
    assert G.number_of_edges == 2

    assert B1 not in G
    assert B2 not in G
    assert B in G

    assert set(G.neighbors(A)) == {B}
    assert set(G.neighbors(C)) == {B}
    assert set(G.neighbors(B)) == {A, C}
