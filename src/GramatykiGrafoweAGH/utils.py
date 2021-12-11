from collections import defaultdict, Iterable
from itertools import groupby
from typing import List, Tuple

import networkx as nx

from GramatykiGrafoweAGH import Node, Production
from GramatykiGrafoweAGH.exceptions import NodeNotFoundError, CannotApplyProductionError, SquareNotFoundError


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


def get_square_vertices(G: nx.Graph, I: Node) -> Tuple[Node, Node, Node, Node]:
    Es = {node for node in G.neighbors(I) if node.label == 'E'}
    if len(Es) != 4:
        raise SquareNotFoundError()

    E1 = min(Es, key=lambda node: (node.x, node.y))
    Es.remove(E1)
    E2 = next(node for node in Es if node in G.neighbors(E1) and node.x >= E1.x)
    Es.remove(E2)
    E4 = next(node for node in Es if node in G.neighbors(E2))
    Es.remove(E4)
    E3, = Es

    return E1, E2, E3, E4


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


def get_nodes_by_position_dict(G: nx.Graph) -> defaultdict:
    d =  defaultdict(list)
    for node in G.nodes:
        d[node.level, node.x, node.y].append(node)
    return d


def check_duplicated_nodes(G: nx.Graph):
    count = sum(1 for nodes in get_nodes_by_position_dict(G).values() if len(nodes) >= 2)
    print(f'{count if count != 0 else "No"} duplicated nodes')
