import matplotlib.pyplot as plt
import networkx as nx

from GramatykiGrafoweAGH.visualization import draw_graph


def make_example_graph() -> nx.Graph:
    G = nx.Graph()

    G.add_node(0, label='e', x=0.5, y=0.5, level=0)

    G.add_node(1, label='i', x=0.5, y=0.5, level=1)
    G.add_node(2, label='E', x=0, y=0, level=1)
    G.add_node(3, label='E', x=1, y=0, level=1)
    G.add_node(4, label='E', x=0, y=1, level=1)
    G.add_node(5, label='E', x=1, y=1, level=1)

    G.add_node(6, label='i', x=0.25, y=0.25, level=2)
    G.add_node(7, label='E', x=0, y=0, level=2)
    G.add_node(8, label='E', x=0.5, y=0, level=2)
    G.add_node(9, label='E', x=0, y=0.5, level=2)
    G.add_node(10, label='E', x=0.5, y=0.5, level=2)

    G.add_node(11, label='I', x=0.125, y=0.125, level=3)
    G.add_node(12, label='E', x=0, y=0, level=3)
    G.add_node(13, label='E', x=0.25, y=0, level=3)
    G.add_node(14, label='E', x=0, y=0.25, level=3)
    G.add_node(15, label='E', x=0.25, y=0.25, level=3)

    G.add_edges_from([
        (0, 1),
        (1, 2), (1, 3), (1, 4), (1, 5),
        (2, 3), (3, 5), (5, 4), (4, 2),
        (1, 6),
        (6, 7), (6, 8), (6, 9), (6, 10),
        (7, 8), (8, 10), (10, 9), (9, 7),
        (6, 11),
        (11, 12), (11, 13), (11, 14), (11, 15),
        (12, 13), (13, 15), (15, 14), (14, 12),
    ])

    return G


if __name__ == '__main__':
    G = make_example_graph()
    draw_graph(G)
    plt.show()
