import networkx as nx
import pytest

from GramatykiGrafoweAGH.project.task5 import P8


def test_P8():
    G = nx.Graph()
    with pytest.raises(NotImplementedError):
        P8(G)
