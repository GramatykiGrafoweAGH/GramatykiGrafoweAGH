import networkx as nx
import pytest

from GramatykiGrafoweAGH.project.task3 import P5, P6


def test_P5():
    G = nx.Graph()
    with pytest.raises(NotImplementedError):
        P5(G)


def test_P6():
    G = nx.Graph()
    with pytest.raises(NotImplementedError):
        P6(G)
