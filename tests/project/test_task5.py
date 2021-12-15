import pytest

from GramatykiGrafoweAGH import Graph
from GramatykiGrafoweAGH.project.task5 import P8


@pytest.mark.xfail(raises=NotImplementedError)
def test_P8():
    G = Graph()
    P8(G)
