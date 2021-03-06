from itertools import combinations

from GramatykiGrafoweAGH import Graph
from GramatykiGrafoweAGH.exceptions import CannotApplyProductionError
from GramatykiGrafoweAGH.project.utils import is_node_between


def P9(G: Graph) -> None:
    for E2s in G.get_duplicates_with_label('E'):
        for E2L, E2R in combinations(E2s, 2):
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
                                                G.merge_two_nodes(E2L, E2R)
                                                return

    raise CannotApplyProductionError()
