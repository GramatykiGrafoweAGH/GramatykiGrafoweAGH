from typing import Iterable, List, Optional

from GramatykiGrafoweAGH import Graph, IProduction, Node
from GramatykiGrafoweAGH.project.utils import is_node_between


class Production8(IProduction):
    def get_possible_roots(self, G: Graph) -> Iterable[Node]:
        for group in G.get_duplicates_with_label('E'):
            yield group[0]

    def check_root(self, G: Graph, root: Node) -> bool:
        return root.label == 'E'

    def match_lhs(self, G: Graph, E2L: Node) -> Optional[List[Node]]:
        for E2R in G.get_duplicates_of(E2L):
            for E1 in G.get_common_neighbors_with_label(E2L, E2R, 'E'):
                for E3L in G.get_neighbors_with_label(E2L, 'E'):
                    if E3L is not E1 and is_node_between(E1, E2L, E3L):
                        for E3R in G.get_duplicates_of(E3L):
                            if E3R is not E1 and is_node_between(E1, E2R, E3R):
                                for I12L in G.get_common_neighbors_with_label(E1, E2L, 'I'):
                                    for I23L in G.get_common_neighbors_with_label(E2L, E3L, 'I'):
                                        for iL in G.get_common_neighbors_with_label(I12L, I23L, 'i'):
                                            for I12R in G.get_common_neighbors_with_label(E1, E2R, 'I'):
                                                for I23R in G.get_common_neighbors_with_label(E2R, E3R, 'I'):
                                                    for iR in G.get_common_neighbors_with_label(I12R, I23R, 'i'):
                                                        for E in G.get_common_neighbors_with_label(iL, iR, 'E'):
                                                            return [E2L, E3L, E2R, E3R]

    def apply_for_lhs(self, G: Graph, lhs: List[Node]) -> List[Node]:
        E2L, E3L, E2R, E3R = lhs
        E2 = G.merge_two_nodes(E2L, E2R)
        E3 = G.merge_two_nodes(E3L, E3R)
        return [E2, E3]


P8 = Production8()
