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
    item1.apply_discount()
    assert item1.price == 1.28
    item2.apply_discount()
    assert item2.price == 1.7


def test_get_total_items():
    Item.all = []
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("banana", 2.0, 5)
    assert Item.get_total_items() == 2


def test_instantiate_from_csv():
    Item.all = [] # очищаем список перед тестом
    Item.instantiate_from_csv('items.csv')
    assert len(Item.all) == 3
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[0].price == 85.0
    assert Item.all[0].quantity == 1
    assert Item.all[1].name == 'Ноутбук'
    assert Item.all[1].price == 850.0
    assert Item.all[1].quantity == 3
    assert Item.all[2].name == 'Кабель'
    assert Item.all[2].price == 8.5
    assert Item.all[2].quantity == 5


if __name__ == '__main__':
    pytest.main()
