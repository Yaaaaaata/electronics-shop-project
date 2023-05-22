import pytest
from item import Item


def test_calculate_total_price():
    item1 = Item("item1", 5.0, 3)
    item2 = Item("item2", 5.0, 2)
    assert item1.calculate_total_price() == 15.0
    assert item2.calculate_total_price() == 10.0


def test_apply_discount():
    item1 = Item("apple", 1.5, 10)
    item2 = Item("banana", 2.0, 5)
    item1.apply_discount(0.1)
    assert item1.price == 1.35
    item2.apply_discount(0.2)
    assert item2.price == 1.6


def test_get_total_items():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("banana", 2.0, 5)
    assert Item.get_total_items() == 2


if __name__ == 'main':
    pytest.main()

