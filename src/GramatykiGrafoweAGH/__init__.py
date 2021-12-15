from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from itertools import count
from typing import List, Iterable, Tuple, Callable

import networkx as nx
from networkx.classes.reportviews import NodeView

from GramatykiGrafoweAGH.exceptions import NodeNotFoundError, CannotApplyProductionError


@dataclass(eq=True, frozen=True)
class Node:
    label: str
    x: float
    y: float
    level: int
    id: int = field(default_factory=count().__next__, init=False)


class NodePositions:
    def __init__(self):
        self._dict = defaultdict(list)

    @staticmethod
    def key(node: Node) -> Tuple[int, float, float]:
        return node.level, node.x, node.y

    def add_node(self, node: Node) -> None:
        self._dict[self.key(node)].append(node)

    def remove_node(self, node: Node) -> None:
        self._dict[self.key(node)].remove(node)

    def get_duplicates_of(self, node: Node) -> Iterable[Node]:
        group = self._dict[node.level, node.x, node.y]
        return [n for n in group if n is not node and n.label == node.label]

    def get_duplicates_with_label(self, label: str) -> Iterable[List[Node]]:
        for group in self._dict.values():
            nodes = [n for n in group if n.label == label]
            if len(nodes) >= 2:
                yield nodes

    def count_duplicates(self) -> int:
        return sum(1 for group in self._dict.values() if len(group) >= 2)


class Graph:
    def __init__(self):
        self._G = nx.Graph()
        self._node_positions = NodePositions()

    def __contains__(self, node: Node) -> bool:
        return self.has_node(node)

    @property
    def nodes(self) -> NodeView:
        return self._G.nodes

    @property
    def number_of_nodes(self) -> int:
        return self._G.number_of_nodes()

    @property
    def number_of_edges(self) -> int:
        return self._G.number_of_edges()

    def add_node(self, node: Node) -> None:
        self._G.add_node(node, node=node)
        self._node_positions.add_node(node)

    def add_nodes(self, nodes: Iterable[Node]) -> None:
        for node in nodes:
            self.add_node(node)

    def add_edge(self, u: Node, v: Node) -> None:
        assert u in self, f'{u} not in graph'
        assert v in self, f'{v} not in graph'
        self._G.add_edge(u, v)

    def add_edges(self, edges: Iterable[Tuple[Node, Node]]):
        for u, v in edges:
            self.add_edge(u, v)

    def has_node(self, node: Node) -> bool:
        return node in self._G

    def remove_node(self, node: Node) -> None:
        self._G.remove_node(node)
        self._node_positions.remove_node(node)

    def remove_nodes(self, nodes: Iterable[Node]) -> None:
        for node in nodes:
            self.remove_node(node)

    def remove_edge(self, u: Node, v: Node) -> None:
        assert u in self, f'{u} not in graph'
        assert v in self, f'{v} not in graph'
        self._G.remove_edge(u, v)

    def replace_node(self, old: Node, new: Node) -> None:
        neighbors = self.neighbors(old)
        self.remove_node(old)
        self.add_node(new)
        self.add_edges((n, new) for n in neighbors)

    def merge_two_nodes(self, old1: Node, old2: Node) -> Node:
        assert old1.label == old2.label and old1.x == old2.x and old1.y == old2.y and old1.level == old2.level
        neighbors = set(self.neighbors(old1)) | set(self.neighbors(old2)) - {old1, old2}
        self.remove_node(old1)
        self.remove_node(old2)
        new = Node(label=old1.label, x=old1.x, y=old1.y, level=old1.level)
        self.add_node(new)
        self.add_edges((n, new) for n in neighbors)
        return new

    def neighbors(self, node: Node):
        return self._G.neighbors(node)

    def get_first_node_with_label(self, label: str) -> Node:
        found = [node for node in self.nodes if node.label == label]
        if not found:
            raise NodeNotFoundError(f'Node with label "{label}" not found')
        return min(found, key=lambda node: (node.level, node.id))

    def get_neighbors_with_label(self, node: Node, label: str) -> List[Node]:
        return [n for n in self.neighbors(node) if n.label == label]

    def get_common_neighbors_with_label(self, a: Node, b: Node, label: str) -> Iterable[Node]:
        for node in self.neighbors(a):
            if node.label == label and node in self.neighbors(b):
                yield node

    def apply_production(self, production: Callable[[Graph], None], *, times: int = 1) -> Graph:
        for _ in range(times):
            production(self)
        return self

    def apply_productions(self, productions: Iterable[Callable[[Graph], None]]) -> Graph:
        for production in productions:
            production(self)
        return self

    def apply_production_while_possible(self, production: Callable[[Graph], None]) -> Graph:
        while True:
            try:
                production(self)
            except CannotApplyProductionError:
                return self

    def get_duplicates_of(self, node: Node) -> Iterable[Node]:
        return self._node_positions.get_duplicates_of(node)

    def get_duplicates_with_label(self, label: str) -> Iterable[List[Node]]:
        return self._node_positions.get_duplicates_with_label(label)

    def count_duplicates(self) -> int:
        return self._node_positions.count_duplicates()

    def assert_no_duplicated_nodes(self) -> None:
        count = self.count_duplicates()
        assert not count, f'There are {count} duplicated nodes'

    def is_isomorphic_with(self, other: Graph) -> bool:
        def node_match(a: dict, b: dict) -> bool:
            a = a['node']
            b = b['node']
            return a.label == b.label and a.x == b.x and a.y == b.y and a.level == b.level

        return nx.is_isomorphic(self._G, other._G, node_match=node_match)

    def show(self):
        from GramatykiGrafoweAGH.visualization import show_graph
        show_graph(self)
