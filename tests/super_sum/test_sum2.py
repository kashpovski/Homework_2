import sum as s
import pytest


@pytest.mark.parametrize("cond, exp", [
    ((1, 2), 3),
    ((-1, 2), 1),
    ((0, -1), -1),
    ((2, 0), 2)
])
def test_positive(cond, exp):
    assert s.sum(*cond) == exp
