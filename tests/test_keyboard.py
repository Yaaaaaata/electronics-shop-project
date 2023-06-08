import pytest
from src.keyboard import Keyboard


def test_keyboard():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert kb.get_language() == "EN"

    kb.change_lang()
    assert kb.get_language() == "RU"

    kb.change_lang().change_lang()
    assert kb.get_language() == "RU"

    kb.language = 'CH'
    assert AttributeError("property 'language' of 'Keyboard' object has no setter")
