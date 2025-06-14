import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import myset_sum

def test_myset_sum():
    assert myset_sum(2, 3) == 5
