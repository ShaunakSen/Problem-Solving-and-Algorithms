import mathlib
import pytest
import sys

@pytest.mark.skipif(sys.version_info > (3,5), reason="Python version > 3.5")
def test_calc_total():
    total = mathlib.calc_total(4, 5)
    assert total == sum([4,5])

def test_calc_prod():
    prod = mathlib.calc_prod(4, 5)
    assert prod == 4*5