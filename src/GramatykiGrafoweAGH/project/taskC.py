from itertools import permutations, combinations

from GramatykiGrafoweAGH import CannotApplyProductionError, Graph, Node, NodeNotFoundError
from GramatykiGrafoweAGH.exceptions import SquareNotFoundError
from GramatykiGrafoweAGH.project.utils import get_square_vertices, is_node_between


def P10(G: Graph) -> None:
    try:
        I = G.get_first_node_with_label('I')
    except NodeNotFoundError:
        raise CannotApplyProductionError()

    level = I.level

    try:
        E1, E2, E3, E4 = get_square_vertices(G, I)
    except SquareNotFoundError:
        raise CannotApplyProductionError()

    x1, y1 = E1.x, E1.y
    x2, y2 = E2.x, E2.y
    x3, y3 = E3.x, E3.y
    x4, y4 = E4.x, E4.y

    i = Node(label='i', x=I.x, y=I.y, level=level)

    I1 = Node(label='I', x=I.x, y=I.y, level=level + 1)

    E1 = Node(label='E', x=x1, y=y1, level=level + 1)
    E2 = Node(label='E', x=x2, y=y2, level=level + 1)
    E3 = Node(label='E', x=x3, y=y3, level=level + 1)
    E4 = Node(label='E', x=x4, y=y4, level=level + 1)

    G.replace_node(I, i)

    G.add_nodes([
        I1,
        E1, E2, E3, E4
    ])

    G.add_edges([
        (i, I1),
        (I1, E1), (I1, E2), (I1, E3), (I1, E4),
        (E1, E2), (E2, E4), (E4, E3), (E3, E1),
    ])


def P11(G: Graph) -> None:
    for E3s in G.get_duplicates_with_label('E'):
        # sides are not symmetric, so we can no longer use combinations
        for E3L, E3R in permutations(E3s, 2):
            for E1R in G.get_neighbors_with_label(E3R, 'E'):
                for E1L in G.get_duplicates_of(E1R):
                    for E2L in G.get_common_neighbors_with_label(E1L, E3L, 'E'):
                        if is_node_between(E1L, E2L, E3L):
                            for I12L in G.get_common_neighbors_with_label(E1L, E2L, 'I'):
                                for I23L in G.get_common_neighbors_with_label(E2L, E3L, 'I'):
                                    for iL in G.get_common_neighbors_with_label(I12L, I23L, 'i'):
                                        for I13R in G.get_common_neighbors_with_label(E1R, E3R, 'I'):
                                            for iR in G.get_neighbors_with_label(I13R, 'i'):
                                                for E in G.get_common_neighbors_with_label(iL, iR, 'E'):
                                                    G.merge_two_nodes(E1L, E1R)
                                                    G.merge_two_nodes(E3L, E3R)
                                                    return

    raise CannotApplyProductionError()


def P12(G: Graph) -> None:
    for E3s in G.get_duplicates_with_label('E'):
        # sides are not symmetric, so we can no longer use combinations
        for E3L, E3R in permutations(E3s, 2):
            for E1 in G.get_neighbors_with_label(E3R, 'E'):
                for E2L in G.get_common_neighbors_with_label(E1, E3L, 'E'):
                    if is_node_between(E1, E2L, E3L):
                        for I12L in G.get_common_neighbors_with_label(E1, E2L, 'I'):
                            for I23L in G.get_common_neighbors_with_label(E2L, E3L, 'I'):
                                for iL in G.get_common_neighbors_with_label(I12L, I23L, 'i'):
                                    for I13R in G.get_common_neighbors_with_label(E1, E3R, 'I'):
                                        for iR in G.get_neighbors_with_label(I13R, 'i'):
                                            for E in G.get_common_neighbors_with_label(iL, iR, 'E'):
                                                G.merge_two_nodes(E3L, E3R)
                                                return

    raise CannotApplyProductionError()


def P13(G: Graph) -> None:
    for E2s in G.get_duplicates_with_label('E'):
        # both sides are symetric, so the order can be arbitrary
        for E2L, E2R in combinations(E2s, 2):
            for I12L in G.get_neighbors_with_label(E2L, 'I'):
                for iL in G.get_neighbors_with_label(I12L, 'i'):
                    for I12R in G.get_neighbors_with_label(E2R, 'I'):
                        for iR in G.get_neighbors_with_label(I12R, 'i'):
                            for E in G.get_common_neighbors_with_label(iL, iR, 'E'):
                                G.merge_two_nodes(E2L, E2R)
                                return

    raise CannotApplyProductionError()
