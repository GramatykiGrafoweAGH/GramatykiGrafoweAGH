import pytest

from GramatykiGrafoweAGH import Graph
from GramatykiGrafoweAGH.project.task4 import P7


def test_P7():
    G = Graph()
    with pytest.raises(NotImplementedError):
        P7(G)
