class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self, discount: float = 0.0) -> None:
        """
        Применяет установленную скидку для конкретного товара.

        :param discount: Размер скидки в процентах.
        """
        self.price *= (1 - discount) * Item.pay_rate

    @classmethod
    def get_total_items(cls) -> int:
        """
        Возвращает количество созданных экземпляров класса Item.

        :return: Количество созданных экземпляров.
        """
        return len(Item.all)
