import networkx as nx
import pytest

from GramatykiGrafoweAGH.project.task2 import P3, P4


def test_P3():
    G = nx.Graph()
    with pytest.raises(NotImplementedError):
        P3(G)


def test_P4():
    G = nx.Graph()
    with pytest.raises(NotImplementedError):
        P4(G)
