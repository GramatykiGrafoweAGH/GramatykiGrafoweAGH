from collections import Callable
from dataclasses import dataclass, field
from functools import wraps
from itertools import count

import networkx as nx


@dataclass(eq=True, frozen=True)
class Node:
    label: str
    x: float
    y: float
    level: int
    id: int = field(default_factory=count().__next__, init=False)


Production = Callable[[nx.Graph], nx.Graph]


def production(func: Callable[[nx.Graph], None]) -> Production:
    @wraps(func)
    def wrapper(G: nx.Graph) -> nx.Graph:
        G = G.copy()
        func(G)
        return G

    return wrapper
