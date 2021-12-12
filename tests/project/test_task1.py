from GramatykiGrafoweAGH.project.task1 import make_initial_graph


def test_make_initial_graph():
    G = make_initial_graph()

    assert G.number_of_nodes() == 1
    assert G.number_of_edges() == 0

    node, = G.nodes

    assert node.label == 'E'
    assert node.x == 0.5
    assert node.y == 0.5
    assert node.level == 0


def test_P1():
    pass


def test_P2():
    pass
