import pytest

from GramatykiGrafoweAGH import Graph
from GramatykiGrafoweAGH.project.task3 import P5, P6


@pytest.mark.xfail(raises=NotImplementedError)
def test_P5():
    G = Graph()
    P5(G)


@pytest.mark.xfail(raises=NotImplementedError)
def test_P6():
    G = Graph()
    P6(G)
