from typing import Tuple
from collections import deque

from GramatykiGrafoweAGH import Node, Graph
from GramatykiGrafoweAGH.exceptions import SquareNotFoundError


def is_node_between(E1: Node, E2: Node, E3: Node) -> bool:
    return E2.x == (E1.x + E3.x) / 2 and E2.y == (E1.y + E3.y) / 2


EPS = 1e-5


def compPos(x1, y1, x2, y2):
    return abs(x1 - x2) < EPS and abs(y1 - y2) < EPS


def get_compatible_neighbours(G: Graph, E: Node, I: Node) -> Tuple[list[Node], list[Tuple[Node, Node]]]:
    nexts = G.get_neighbors_with_label(E, 'E')
    res = [], []
    for next in nexts:
        if I in G.get_neighbors_with_label(next, 'I'):
            res[0].append(next)
        else:
            x1, y1 = E.x, E.y
            x2, y2 = next.x, next.y
            x3, y3 = x2 + (x2 - x1), y2 + (y2 - y1)
            nexts2 = filter(lambda e: I in G.get_neighbors_with_label(e, 'I') and compPos(e.x, e.y, x3, y3), G.get_neighbors_with_label(next, 'E'))
            res[1].extend(list(map(lambda e: (next, e), nexts2)))

    return res


def dfs(poss, start, target, path, visited, level):
    if level == 4:
        if start == target:
            return path
        else:
            return None

    nexts = poss[start]

    for next in nexts[0]:
        if next in visited:
            continue
        res = dfs(poss, next, target, path + [(None, next)], visited + [next], level + 1)
        if res is not None:
            return res

    for step, next in nexts[1]:
        if next in visited:
            continue
        res = dfs(poss, next, target, path + [(step, next)], visited + [step, next], level + 1)
        if res is not None:
            return res

    return None


def get_square_vertices_extended(G: Graph, I: Node):
    Es = G.get_neighbors_with_label(I, 'E')
    if len(Es) < 4:
        raise SquareNotFoundError()

    possibilities = {e: get_compatible_neighbours(G, e, I) for e in Es}

    for E in Es:
        path = dfs(possibilities, E, E, [], [], 0)
        if path is not None:
            break
    else:
        raise SquareNotFoundError()

    (E10, E00), (E01, E02), (E12, E22), (E21, E20) = path
    corners = [E00, E02, E22, E20]
    edges = [E01, E12, E21, E10]
    eCount = len(list(filter(lambda x: x is not None, edges)))
    if eCount == 0 or eCount == 4:
        return corners, edges

    corners, edges = deque(corners), deque(edges)
    for _ in range(4):
        if edges[0] is not None and edges[-1] is None:
            break
        corners.rotate(1)
        edges.rotate(1)
    return list(corners), list(edges)


def get_square_vertices(G: Graph, I: Node) -> Tuple[Node, Node, Node, Node]:
    [E00, E02, E22, E20], _ = get_square_vertices_extended(G, I)

    return E00, E02, E20, E22
