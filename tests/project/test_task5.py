import pytest

from GramatykiGrafoweAGH import Graph
from GramatykiGrafoweAGH.project.task5 import P8


def test_P8():
    G = Graph()
    with pytest.raises(NotImplementedError):
        P8(G)
