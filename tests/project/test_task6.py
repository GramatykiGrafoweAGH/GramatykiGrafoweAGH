import pytest

from GramatykiGrafoweAGH import Graph
from GramatykiGrafoweAGH.project.task6 import P9


def test_P9():
    G = Graph()
    with pytest.raises(NotImplementedError):
        P9(G)
