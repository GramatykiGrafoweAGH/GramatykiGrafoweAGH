from typing import Tuple

from GramatykiGrafoweAGH import Node, Graph
from GramatykiGrafoweAGH.exceptions import SquareNotFoundError


def is_node_between(E1: Node, E2: Node, E3: Node) -> bool:
    return E2.x == (E1.x + E3.x) / 2 and E2.y == (E1.y + E3.y) / 2


def get_square_vertices(G: Graph, I: Node) -> Tuple[Node, Node, Node, Node]:
    Es = G.get_neighbors_with_label(I, 'E')
    if len(Es) != 4:
        raise SquareNotFoundError()

    E3 = min(Es, key=lambda node: (node.x, node.y))
    Es.remove(E3)
    E2 = max(Es, key=lambda node: (node.x, node.y))
    Es.remove(E2)
    E4 = max(Es, key=lambda node: node.x)
    Es.remove(E4)
    E1, = Es

    return E1, E2, E3, E4
