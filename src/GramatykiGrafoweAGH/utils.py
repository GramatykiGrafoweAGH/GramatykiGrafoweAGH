from collections import defaultdict
from typing import Callable, Iterable, List, Tuple

import networkx as nx

from GramatykiGrafoweAGH import Node
from GramatykiGrafoweAGH.exceptions import NodeNotFoundError, CannotApplyProductionError, SquareNotFoundError


def get_first_node_with_label(G: nx.Graph, label: str) -> Node:
    found = [node for node in G.nodes if node.label == label]
    if not found:
        raise NodeNotFoundError(f'Node with label "{label}" not found')
    return min(found, key=lambda node: (node.level, node.id))


def get_neighbors_with_label(G: nx.Graph, node: Node, label: str) -> List[Node]:
    return [n for n in G.neighbors(node) if n.label == label]


def get_common_neighbors_with_label(G: nx.Graph, a: Node, b: Node, label: str) -> Iterable[Node]:
    for node in G.neighbors(a):
        if node.label == label and node in G.neighbors(b):
            yield node


def get_square_vertices(G: nx.Graph, I: Node) -> Tuple[Node, Node, Node, Node]:
    Es = get_neighbors_with_label(G, I, 'E')
    if len(Es) != 4:
        raise SquareNotFoundError()

    E1 = min(Es, key=lambda node: (node.x, node.y))
    Es.remove(E1)
    E2 = next(node for node in Es if node in G.neighbors(E1) and node.x > E1.x)
    Es.remove(E2)
    E4 = next(node for node in Es if node in G.neighbors(E2))
    Es.remove(E4)
    E3, = Es

    return E1, E2, E3, E4


def is_node_between(E1: Node, E2: Node, E3: Node) -> bool:
    return E2.x == (E1.x + E3.x) / 2 and E2.y == (E1.y + E3.y) / 2


class NodePositions:
    def __init__(self, G: nx.Graph):
        self._dict = defaultdict(list)
        for node in G.nodes:
            self._dict[node.level, node.x, node.y].append(node)

    def groups(self) -> Iterable[List[Node]]:
        return self._dict.values()

    def duplicates(self, label: str) -> Iterable[List[Node]]:
        for group in self.groups():
            nodes = [n for n in group if n.label == label]
            if len(nodes) >= 2:
                yield nodes

    def get_duplicates_of(self, node: Node) -> Iterable[Node]:
        nodes = self._dict[node.level, node.x, node.y]
        return [n for n in nodes if n is not node and n.label == node.label]

    def count_duplicated_nodes(self) -> int:
        return sum(1 for nodes in self._dict.values() if len(nodes) >= 2)


def assert_no_duplicated_nodes(G: nx.Graph) -> None:
    count = NodePositions(G).count_duplicated_nodes()
    assert not count, f'There are {count} duplicated nodes'


def replace_node(G: nx.Graph, old: Node, new: Node):
    neighbors = G.neighbors(old)
    G.remove_node(old)
    G.add_node(new)
    G.add_edges_from((n, new) for n in neighbors)


def merge_two_nodes(G: nx.Graph, old1: Node, old2: Node) -> Node:
    assert old1.label == old2.label and old1.x == old2.x and old1.y == old2.y and old1.level == old2.level
    neighbors = set(G.neighbors(old1)) | set(G.neighbors(old2)) - {old1, old2}
    G.remove_node(old1)
    G.remove_node(old2)
    new = Node(label=old1.label, x=old1.x, y=old1.y, level=old1.level)
    G.add_node(new)
    G.add_edges_from((n, new) for n in neighbors)
    return new


def apply_productions(G: nx.Graph, productions: Iterable[Callable[[nx.Graph], Node]]) -> nx.Graph:
    for production in productions:
        production(G)
    return G


def apply_production_while_possible(G: nx.Graph, production: Callable[[nx.Graph], Node]) -> nx.Graph:
    while True:
        try:
            G = production(G)
        except CannotApplyProductionError:
            return G
