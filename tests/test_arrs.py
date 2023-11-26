from utils.arrs import get
from utils.arrs import my_slice


def test_get():
    assert get([1, 2, 3], 1, "test") == 2
    assert get([], 0, "test") == "test"
    assert get([1, 2, 3], -1, "test") == "test"
    assert get([1, 2, 3], 5, "test") == "test"


def test_slice():
    assert my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert my_slice([1, 2, 3], 1) == [2, 3]
    assert my_slice([], 0, 2) == []
    assert my_slice([1, 2, 3], end=5) == [1, 2, 3]