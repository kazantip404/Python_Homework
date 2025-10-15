import pytest
from string_utils import StringUtils

# Создаем экземпляр класса для тестирования.
string_utils = StringUtils()


# ============================================================
# ТЕСТЫ ДЛЯ МЕТОДА capitalize
# ============================================================

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    # Тест 1: Обычная строка с маленькой буквы
    ("skypro", "Skypro"),
    # Тест 2: Строка с пробелом
    ("hello world", "Hello world"),
    # Тест 3: Другая обычная строка
    ("python", "Python"),
    # Тест 4: Строка с цифрой в начале (должна остаться без изменений)
    ("1skypro", "1skypro"),
])
def test_capitalize_positive(input_str, expected):
    """Позитивные тесты для метода capitalize"""
    result = string_utils.capitalize(input_str)
    assert result == expected, f"Ожидалось: '{expected}', Получено: '{result}'"


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    # Тест 1: Строка начинающаяся с цифры
    ("123abc", "123abc"),
    # Тест 2: Пустая строка
    ("", ""),
    # Тест 3: Строка из пробелов
    ("   ", "   "),
    # Тест 4: Строка с заглавной буквы (должна остаться без изменений)
    ("Skypro", "Skypro"),
])
def test_capitalize_negative(input_str, expected):
    """Негативные тесты для метода capitalize"""
    result = string_utils.capitalize(input_str)
    assert result == expected, f"Ожидалось: '{expected}', Получено: '{result}'"


# ============================================================
# ТЕСТЫ ДЛЯ МЕТОДА trim
# ============================================================

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    # Тест 1: Строка с несколькими пробелами в начале
    ("   skypro", "skypro"),
    # Тест 2: Строка с двумя пробелами в начале
    ("  hello", "hello"),
    # Тест 3: Строка с пробелами в начале и конце (удаляются только начальные)
    ("    python  ", "python  "),
    # Тест 4: Строка с одним пробелом в начале
    (" test", "test"),
])
def test_trim_positive(input_str, expected):
    """Позитивные тесты для метода trim"""
    result = string_utils.trim(input_str)
    assert result == expected, f"Ожидалось: '{expected}', Получено: '{result}'"


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    # Тест 1: Строка без пробелов в начале
    ("skypro", "skypro"),
    # Тест 2: Пустая строка
    ("", ""),
    # Тест 3: Строка с пробелами только в конце
    ("test   ", "test   "),
    # Тест 4: Строка с пробелами в середине
    ("hello world", "hello world"),
])
def test_trim_negative(input_str, expected):
    """Негативные тесты для метода trim"""
    result = string_utils.trim(input_str)
    assert result == expected, f"Ожидалось: '{expected}', Получено: '{result}'"


# ============================================================
# ТЕСТЫ ДЛЯ МЕТОДА contains
# ============================================================

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    # Тест 1: Поиск заглавной буквы
    ("SkyPro", "S", True),
    # Тест 2: Поиск строчной буквы
    ("SkyPro", "k", True),
    # Тест 3: Поиск буквы в конце строки
    ("SkyPro", "o", True),
    # Тест 4: Поиск пробела
    ("Hello World", " ", True),
    # Тест 5: Поиск подстроки из нескольких символов
    ("SkyPro", "Sky", True),
])
def test_contains_positive(string, symbol, expected):
    """Позитивные тесты для метода contains"""
    result = string_utils.contains(string, symbol)
    assert result == expected, f"Строка: '{string}', Символ: '{symbol}' - Ожидалось: {expected}, Получено: {result}"


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    # Тест 1: Поиск отсутствующего символа
    ("SkyPro", "U", False),
    # Тест 2: Поиск символа в неправильном регистре
    ("SkyPro", "s", False),
    # Тест 3: Поиск в пустой строке
    ("", "a", False),
    # Тест 4: Поиск отсутствующего символа
    ("Hello", "x", False),
    # Тест 5: Поиск длинной отсутствующей подстроки
    ("SkyPro", "SkyPro123", False),
])
def test_contains_negative(string, symbol, expected):
    """Негативные тесты для метода contains"""
    result = string_utils.contains(string, symbol)
    assert result == expected, f"Строка: '{string}', Символ: '{symbol}' - Ожидалось: {expected}, Получено: {result}"


# ============================================================
# ТЕСТЫ ДЛЯ МЕТОДА delete_symbol
# ============================================================

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    # Тест 1: Удаление одного символа
    ("SkyPro", "k", "SyPro"),
    # Тест 2: Удаление подстроки
    ("SkyPro", "Pro", "Sky"),
    # Тест 3: Удаление пробела
    ("Hello World", " ", "HelloWorld"),
    # Тест 4: Удаление всех вхождений символа
    ("banana", "a", "bnn"),
    # Тест 5: Удаление цифры
    ("test123", "1", "test23"),
])
def test_delete_symbol_positive(string, symbol, expected):
    """Позитивные тесты для метода delete_symbol"""
    result = string_utils.delete_symbol(string, symbol)
    assert result == expected, f"Строка: '{string}', Символ: '{symbol}' - Ожидалось: '{expected}', Получено: '{result}'"


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    # Тест 1: Удаление отсутствующего символа
    ("SkyPro", "X", "SkyPro"),
    # Тест 2: Удаление отсутствующего символа
    ("Hello", "z", "Hello"),
    # Тест 3: Удаление из пустой строки
    ("", "a", ""),
    # Тест 4: Удаление пустой подстроки
    ("Test", "", "Test"),
    # Тест 5: Удаление отсутствующей подстроки
    ("SkyPro", "Java", "SkyPro"),
])
def test_delete_symbol_negative(string, symbol, expected):
    """Негативные тесты для метода delete_symbol"""
    result = string_utils.delete_symbol(string, symbol)
    assert result == expected, f"Строка: '{string}', Символ: '{symbol}' - Ожидалось: '{expected}', Получено: '{result}'"
