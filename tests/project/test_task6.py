import pytest

from GramatykiGrafoweAGH import Graph
from GramatykiGrafoweAGH.project.task6 import P9


@pytest.mark.xfail(raises=NotImplementedError)
def test_P9():
    G = Graph()
    P9(G)
