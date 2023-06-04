import pytest
from src.phone import Phone


def test_number_of_sim():
    phone = Phone("iPhone", 1000, 5, 2)
    assert phone.number_of_sim == 2

    with pytest.raises(ValueError):
        phone.number_of_sim = -1

    phone.number_of_sim = 0
    assert phone.number_of_sim == 1
