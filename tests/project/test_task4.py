import pytest

from GramatykiGrafoweAGH import Graph
from GramatykiGrafoweAGH.project.task4 import P7


@pytest.mark.xfail(raises=NotImplementedError)
def test_P7():
    G = Graph()
    P7(G)
