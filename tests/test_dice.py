
from pyencountersim.dice import roll, roll20
import pytest

def test_basic_roll():
    result = [roll('1d6') for i in range(10)]
    assert min(result) >= 1
    assert max(result) <= 6

def test_multi_roll():
    result = roll('5d1')
    assert result == 5

def test_mod_roll_pos():
    result = [roll('2d10+5') for i in range(1000)]
    assert min(result) == 7
    assert max(result) == 25

def test_mod_roll_neg():
    result = [roll('1d4-4') for i in range(1000)]
    assert min(result) == -3
    assert max(result) == 0

def test_bad_roll_str():
    with pytest.raises(ValueError):
        roll("2000")

    with pytest.raises(ValueError):
        roll("bob")

    with pytest.raises(ValueError):
        roll("1d")

def test_d20():
    result = [roll20() for i in range(1000)]
    raws = [r[0] for r in result]
    totals = [r[1] for r in result]
    assert min(raws) == 1
    assert max(raws) == 20
    assert min(totals) == 1
    assert max(totals) == 20

def test_mod_d20():
    result = [roll20(5) for i in range(1000)]
    raws = [r[0] for r in result]
    totals = [r[1] for r in result]
    assert min(raws) == 1
    assert max(raws) == 20
    assert min(totals) == 6
    assert max(totals) == 25

