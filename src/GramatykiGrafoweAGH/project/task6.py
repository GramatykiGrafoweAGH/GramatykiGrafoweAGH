from itertools import combinations
from typing import Iterable, List, Optional

from GramatykiGrafoweAGH import Graph, IProduction, Node
from GramatykiGrafoweAGH.project.utils import is_node_between


class Production9(IProduction):
    def get_possible_roots(self, G: Graph) -> Iterable[Node]:
        for group in G.get_duplicates_with_label('E'):
            yield from group

    def check_root(self, G: Graph, root: Node) -> bool:
        return root.label == 'E'

    def match_lhs(self, G: Graph, E2L: Node) -> Optional[List[Node]]:
        for E2R in G.get_duplicates_of(E2L):
            E13s = G.get_common_neighbors_with_label(E2L, E2R, 'E')
            for E1, E3 in combinations(E13s, 2):
                if is_node_between(E1, E2L, E3) and is_node_between(E1, E2R, E3):
                    for I12L in G.get_common_neighbors_with_label(E1, E2L, 'I'):
                        for I23L in G.get_common_neighbors_with_label(E2L, E3, 'I'):
                            for iL in G.get_common_neighbors_with_label(I12L, I23L, 'i'):
                                for I12R in G.get_common_neighbors_with_label(E1, E2R, 'I'):
                                    for I23R in G.get_common_neighbors_with_label(E2R, E3, 'I'):
                                        for iR in G.get_common_neighbors_with_label(I12R, I23R, 'i'):
                                            for E in G.get_common_neighbors_with_label(iL, iR, 'E'):
                                                return [E2L, E2R]

    def apply_for_lhs(self, G: Graph, lhs: List[Node]) -> List[Node]:
        E2L, E2R = lhs
        E2 = G.merge_two_nodes(E2L, E2R)
        return [E2]


P9 = Production9()
