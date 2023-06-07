from src.item import Item


class LanguageMixin:
    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value not in ['EN', 'RU']:
            print(AttributeError("property 'language' of 'Keyboard' object has no setter"))
        self._language = value

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'
        return self


class Keyboard(Item, LanguageMixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)

    def __str__(self):
        return self.get_name() 

    def get_language(self):
        return self.language

    def change_lang(self):
        super().change_lang()
        return self

    def get_name(self):
        return self.name
