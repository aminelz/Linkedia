import pytest

from src.backend.mining.main import addition


def test_addition__simplecase():
    x = 3
    y = 2
    expected_z = 5

    assert addition(x, y) == expected_z


@pytest.mark.skip(reason="Used to test git workflow")
def test_addition__failingcase():
    x = 3
    y = 2
    expected_z = 0

    assert addition(x, y) == expected_z
