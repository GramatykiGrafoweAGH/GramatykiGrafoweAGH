from typing import Iterable, List, Optional

from GramatykiGrafoweAGH import Graph, IProduction, Node


class Production3(IProduction):
    def get_possible_roots(self, G: Graph) -> Iterable[Node]:
        raise NotImplementedError()

    def check_root(self, G: Graph, root: Node) -> bool:
        raise NotImplementedError()

    def match_lhs(self, G: Graph, root: Node) -> Optional[List[Node]]:
        raise NotImplementedError()

    def apply_for_lhs(self, G: Graph, lhs: List[Node]) -> List[Node]:
        raise NotImplementedError()


class Production4(IProduction):
    def get_possible_roots(self, G: Graph) -> Iterable[Node]:
        raise NotImplementedError()

    def check_root(self, G: Graph, root: Node) -> bool:
        raise NotImplementedError()

    def match_lhs(self, G: Graph, root: Node) -> Optional[List[Node]]:
        raise NotImplementedError()

    def apply_for_lhs(self, G: Graph, lhs: List[Node]) -> List[Node]:
        raise NotImplementedError()


P3 = Production3()
P4 = Production4()
