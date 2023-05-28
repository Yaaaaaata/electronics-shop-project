import csv
import os
import math


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name if len(name) <= 10 else ''
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self) -> str:
        """
        Возвращает название товара.

        :return: Название товара.
        """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """
        Устанавливает название товара.

        :param value: Новое название товара.
        """
        if len(value) > 10:
            return
        self.__name = value

    @name.getter
    def name(self):
        return self.__name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return self.__name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = round(self.price * Item.pay_rate, 2)

    @classmethod
    def get_total_items(cls) -> int:
        """
        Возвращает количество созданных экземпляров класса Item.

        :return: Количество созданных экземпляров.
        """
        return math.floor(float(len([item for item in Item.all if item.name])))

    @classmethod
    def instantiate_from_csv(cls, filename: str) -> None:
        """
        Создает экземпляры класса Item из данных CSV-файла.

        :param filename: Имя CSV-файла.
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, filename)
        with open(file_path, newline='', encoding='windows-1251') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)

    @staticmethod
    def string_to_number(value: str) -> float:
        """
        Преобразует числовую строку в число.

        :param value: Числовая строка.
        :return: Число.
        """
        return float(value.replace(',', '.'))
