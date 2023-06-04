import pytest
from src.item import Item


def test_calculate_total_price():
    item1 = Item("item1", 5.0, 3)
    item2 = Item("item2", 5.0, 2)
    assert item1.calculate_total_price() == 15.0
    assert item2.calculate_total_price() == 10.0


def test_apply_discount():
    item1 = Item("apple", 1.5, 10)
    item2 = Item("banana", 2.0, 5)
    item1.apply_discount()
    assert item1.price == 1.27
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
    assert len(Item.all) == 4
    assert Item.all[0].name == 'Ноутбук'
    assert Item.all[0].price == 1000.0
    assert Item.all[0].quantity == 3
    assert Item.all[1].name == 'Кабель'
    assert Item.all[1].price == 10
    assert Item.all[1].quantity == 5
    assert Item.all[2].name == 'Мышка'
    assert Item.all[2].price == 50
    assert Item.all[2].quantity == 5


def test_item_repr():
    i = Item('test', 10.0, 5)
    assert repr(i) == "Item('test', 10.0, 5)"


def test_item_str():
    i = Item('test', 10.0, 5)
    assert str(i) == 'test'


def test_add():
    item1 = Item("item1", 10, 3)
    item2 = Item("item2", 20, 5)

    assert item1.__add__(item2) == 8

    with pytest.raises(TypeError):
        item1.__add__("not an item")


if __name__ == '__main__':
    pytest.main()
