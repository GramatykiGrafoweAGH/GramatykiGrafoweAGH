import networkx as nx
import pytest

from GramatykiGrafoweAGH.project.task4 import P7


def test_P7():
    G = nx.Graph()
    with pytest.raises(NotImplementedError):
        P7(G)
