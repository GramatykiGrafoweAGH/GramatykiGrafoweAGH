from GramatykiGrafoweAGH import CannotApplyProductionError
import pytest


def assert_production_cannot_be_applied(P, G):
    with pytest.raises(CannotApplyProductionError):
        P(G)
