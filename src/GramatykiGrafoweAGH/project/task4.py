from itertools import combinations

from GramatykiGrafoweAGH import Graph
from GramatykiGrafoweAGH.exceptions import CannotApplyProductionError
from GramatykiGrafoweAGH.project.utils import is_node_between


def P7(G: Graph) -> None:
    for E2s in G.get_duplicates_with_label('E'):
        for E2L, E2R in combinations(E2s, 2):
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
                                                            G.merge_two_nodes(E1L, E1R)
                                                            G.merge_two_nodes(E2L, E2R)
                                                            G.merge_two_nodes(E3L, E3R)
                                                            return

    raise CannotApplyProductionError()
