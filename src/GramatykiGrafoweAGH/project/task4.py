from itertools import combinations

from GramatykiGrafoweAGH import Graph
from GramatykiGrafoweAGH.exceptions import CannotApplyProductionError
from GramatykiGrafoweAGH.project.utils import is_node_between


def P7(G: Graph) -> None:
    for E2s in G.get_duplicates_with_label('E'):
        for E2L, E2R in combinations(E2s, 2):
            E1L_, E2L_, E3L_ = None, None, None
            E1R_, E2R_, E3R_ = None, None, None

            E13Ls = G.get_neighbors_with_label(E2L, 'E')
            # both sides are symetric, so the order can be arbitrary
            for E1L, E3L in combinations(E13Ls, 2):
                if is_node_between(E1L, E2L, E3L):
                    E1L_, E2L_, E3L_ = E1L, E2L, E3L

            if E1L_ is not None:
                for E1R in G.get_duplicates_of(E1L_):
                    for E3R in G.get_duplicates_of(E3L_):
                        if is_node_between(E1R, E2R, E3R):
                            E1R_, E2R_, E3R_ = E1R, E2R, E3R

            if E1L_ is not None and E1R_ is not None:
                for I12L in G.get_common_neighbors_with_label(E1L_, E2L_, 'I'):
                    for I23L in G.get_common_neighbors_with_label(E2L_, E3L_, 'I'):
                        for iL in G.get_common_neighbors_with_label(I12L, I23L, 'i'):
                            for I12R in G.get_common_neighbors_with_label(E1R_, E2R_, 'I'):
                                for I23R in G.get_common_neighbors_with_label(E2R_, E3R_, 'I'):
                                    for iR in G.get_common_neighbors_with_label(I12R, I23R, 'i'):
                                        for E in G.get_common_neighbors_with_label(iL, iR, 'E'):
                                            G.merge_two_nodes(E1L_, E1R_)
                                            G.merge_two_nodes(E2L_, E2R_)
                                            G.merge_two_nodes(E3L_, E3R_)
                                            return

    raise CannotApplyProductionError()
