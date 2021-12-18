from itertools import combinations
from typing import Optional, Iterable, List

from GramatykiGrafoweAGH import Graph, IProduction, Node
from GramatykiGrafoweAGH.project.utils import is_node_between


class Production7(IProduction):
    def get_possible_roots(self, G: Graph) -> Iterable[Node]:
        for group in G.get_duplicates_with_label('E'):
            yield group[0]

    def match_lhs(self, G: Graph, E2L: Node) -> Optional[List[Node]]:
        if E2L.label != 'E':
            return None

        for E2R in G.get_duplicates_of(E2L):
            E13Ls = G.get_neighbors_with_label(E2L, 'E')
            for E1L, E3L in combinations(E13Ls, 2):
                if is_node_between(E1L, E2L, E3L):
                    for E1R in G.get_duplicates_of(E1L):
                        for E3R in G.get_duplicates_of(E3L):
                            if is_node_between(E1R, E2R, E3R):
                                for I12L in G.get_common_neighbors_with_label(E1L, E2L, 'I'):
                                    for I23L in G.get_common_neighbors_with_label(E2L, E3L, 'I'):
                                        for iL in G.get_common_neighbors_with_label(I12L, I23L, 'i'):
                                            for I12R in G.get_common_neighbors_with_label(E1R, E2R, 'I'):
                                                for I23R in G.get_common_neighbors_with_label(E2R, E3R, 'I'):
                                                    for iR in G.get_common_neighbors_with_label(I12R, I23R, 'i'):
                                                        for E in G.get_common_neighbors_with_label(iL, iR, 'E'):
                                                            return [E1L, E2L, E3L, E1R, E2R, E3R]

    def apply(self, G: Graph, lhs: List[Node]) -> List[Node]:
        E1L, E2L, E3L, E1R, E2R, E3R = lhs
        E1 = G.merge_two_nodes(E1L, E1R)
        E2 = G.merge_two_nodes(E2L, E2R)
        E3 = G.merge_two_nodes(E3L, E3R)
        return [E1, E2, E3]


P7 = Production7()
