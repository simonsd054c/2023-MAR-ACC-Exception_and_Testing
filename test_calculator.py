import pytest
from calculator import add, subtract, division, convert_into_list, get_user_input_and_double, get_user_input_and_add

def test_basic():
    assert "hello" == "hello"

def test_add():
    assert add(1, 2) == 3
    assert add(5, 3) == 8

def test_subtract():
    assert subtract(10, 2) == 8
    assert subtract(-5, -7) == 2

def test_division():
    assert division(10, 5) == 2

def test_division_raise_error():
    with pytest.raises(Exception):
        division(10, 0)

def test_convert():
    assert 5 in convert_into_list(3, 4, 5)
    assert 15 not in convert_into_list(7, 8, 9)

def test_user_input_double(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")
    assert get_user_input_and_double() == 6
    monkeypatch.setattr("builtins.input", lambda _: "6")
    assert get_user_input_and_double() == 12

def test_user_input_add(monkeypatch):
    inputs = iter(["3", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_user_input_and_add() == 7