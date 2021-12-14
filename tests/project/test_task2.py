import pytest

from GramatykiGrafoweAGH import Graph
from GramatykiGrafoweAGH.project.task2 import P3, P4


def test_P3():
    G = Graph()
    with pytest.raises(NotImplementedError):
        P3(G)


def test_P4():
    G = Graph()
    with pytest.raises(NotImplementedError):
        P4(G)
