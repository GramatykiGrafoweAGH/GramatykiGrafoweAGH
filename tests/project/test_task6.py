import networkx as nx
import pytest

from GramatykiGrafoweAGH.project.task6 import P9


def test_P9():
    G = nx.Graph()
    with pytest.raises(NotImplementedError):
        P9(G)

