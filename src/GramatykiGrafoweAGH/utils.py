from collections import Iterable
from typing import List

import networkx as nx

from GramatykiGrafoweAGH import Node, Production
from GramatykiGrafoweAGH.exceptions import NodeNotFoundError, CannotApplyProductionError


def find_nodes_with_label(G: nx.Graph, label: str) -> List[Node]:
    return sorted(
        (node for node in G.nodes if node.label == label),
        key=lambda node: (node.level, node.id)
    )


def find_node_with_label(G: nx.Graph, label: str) -> Node:
    found = find_nodes_with_label(G, label)
    if not found:
        raise NodeNotFoundError(f'Node with label "{label}" not found')
    return found[0]


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


def apply_productions(G: nx.Graph, productions: Iterable[Production]) -> nx.Graph:
    # TODO: use itertools.reduce
    for production in productions:
        G = production(G)
    return G


def apply_production_while_possible(G: nx.Graph, production: Production) -> nx.Graph:
    while True:
        try:
            G = production(G)
        except CannotApplyProductionError:
            return G
