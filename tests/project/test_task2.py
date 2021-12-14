import pytest

from GramatykiGrafoweAGH import Graph
from GramatykiGrafoweAGH.project.task2 import P3, P4


@pytest.mark.xfail(raises=NotImplementedError)
def test_P3():
    G = Graph()
    P3(G)


@pytest.mark.xfail(raises=NotImplementedError)
def test_P4():
    G = Graph()
    P4(G)
