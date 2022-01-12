from GramatykiGrafoweAGH import Graph, Node
from GramatykiGrafoweAGH.project.taskC import P10
from GramatykiGrafoweAGH.testing import assert_production_cannot_be_applied


def make_P10_left_side_graph():
    G = Graph()

    level = 1
    x0, y0 = 0, 0
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


def make_P10_right_side_graph():
    G = Graph()

    level = 1
    x0, y0 = 0, 0
    x1, y1 = -0.5, -0.5
    x2, y2 = 0.5, -0.5
    x3, y3 = -0.5, 0.5
    x4, y4 = 0.5, 0.5

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

    I = Node(label='I', x=x0, y=y0, level=level + 2)
    E1 = Node(label='E', x=x1, y=y1, level=level + 2)
    E2 = Node(label='E', x=x2, y=y2, level=level + 2)
    E3 = Node(label='E', x=x3, y=y3, level=level + 2)
    E4 = Node(label='E', x=x4, y=y4, level=level + 2)

    G.add_nodes([I, E1, E2, E3, E4])

    G.add_edges([
        (I, i),
        (I, E1), (I, E2), (I, E3), (I, E4),
        (E1, E2), (E2, E4), (E4, E3), (E3, E1),
    ])

    return G


def test_P10_isomorphic_left_side():
    # test application of P10 to the graph isomorphic to left side of P10
    G = make_P10_left_side_graph()

    P10(G)

    assert G.number_of_nodes == 10

    assert G.number_of_edges == 17

    Es1 = G.get_nodes_with_predicate(lambda n: n.level == 2 and n.label == 'E')

    assert len(Es1) == 4

    Es2 = G.get_nodes_with_predicate(lambda n: n.level == 3 and n.label == 'E')

    assert len(Es2) == 4

    Is = G.get_nodes_with_predicate(lambda n: n.label == 'I')

    assert len(Is) == 1

    iss = G.get_nodes_with_predicate(lambda n: n.label == 'i')

    assert len(iss) == 1

    G.is_isomorphic_with(make_P10_right_side_graph())


def test_P10_left_side_deleted_node():
    # test application of P10 to the graph isomorphic to left side of P10 with deleted one node
    G = make_P10_left_side_graph()
    E = G.get_first_node_with_label('E')
    G.remove_node(E)

    assert_production_cannot_be_applied(P10, G)


def test_P10_left_side_deleted_edge():
    # test application of P10 to the graph isomorphic to left side of P10 with deleted one edge
    G = make_P10_left_side_graph()
    E = G.get_first_node_with_label('E')
    G.remove_edge(E, list(G.get_neighbors(E))[0])

    assert_production_cannot_be_applied(P10, G)


def test_P10_left_side_wrong_label():
    # test application of P10 to the graph isomorphic to left side of P10 with not appropiate label
    G = make_P10_left_side_graph()
    E = G.get_first_node_with_label('E')
    G.replace_node(E, Node(label='e', x=E.x, y=E.y, level=E.level))

    assert_production_cannot_be_applied(P10, G)


def test_P10_left_side_subgraph():
    # test application of P10 to the graph with the subgraph isomorphic to left side of P10
    G = make_P10_left_side_graph()
    expected = make_P10_right_side_graph()

    def add_node(G: Graph) -> None:
        E = G.get_first_node_with_label('E')
        S = Node(label='S', x=-1, y=-1, level=2)
        G.add_node(S)
        G.add_edge(E, S)

    add_node(G)
    add_node(expected)

    P10(G)

    assert G.is_isomorphic_with(expected)


def test_P10_left_side_invariance():
    # test invariance of the left side graph when production cannot be applied
    G = make_P10_left_side_graph()
    expected = make_P10_left_side_graph()

    def remove_node(G: Graph) -> None:
        E = G.get_first_node_with_label('E')
        G.remove_node(E)

    remove_node(G)
    remove_node(expected)

    assert_production_cannot_be_applied(P10, G)
    assert G.is_isomorphic_with(expected)


def test_P10_can_be_applied_many_times():
    G = make_P10_left_side_graph()

    G.apply_production(P10, times=100)

    iss = G.get_nodes_with_predicate(lambda n: n.label == 'i')
    assert len(iss) == 100
