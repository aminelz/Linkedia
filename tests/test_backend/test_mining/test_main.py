from src.backend.mining.main import addition


def test_addition__simplecase():
    x = 3
    y = 2
    expected_z = 5

    assert addition(x, y) == expected_z
