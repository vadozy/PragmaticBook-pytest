import pytest

@pytest.mark.skip()
def test_failing():
    print("Vadim1")  # Use -s switch to see on console
    assert (1, 2, 3) == (3, 2, 1)

@pytest.mark.xfail()
def test_failing2():
    print("Vadim2")  # Use -s switch to see on console
    assert (1, 2, 3) == (3, 2, 1)
