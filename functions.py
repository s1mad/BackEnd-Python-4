"""
Функции для демонстрации работы исключений.
"""

from exceptions import InvalidValueError, DivisionByNegativeError, ResourceNotFoundError


# Шаг 1
def divide(a, b):
    """Функция для деления, выбрасывает исключение при делении на ноль"""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b


def multiply_positive(a, b):
    """Функция для умножения, выбрасывает исключение, если одно из чисел отрицательное"""
    if a < 0 or b < 0:
        raise ValueError("Числа должны быть положительными")
    return a * b


# Шаг 2
def get_element_from_list(lst, index):
    """Функция для получения элемента списка, выбрасывает исключение при неправильном индексе"""
    try:
        return lst[index]
    except Exception as e:
        print(f"Ошибка: {e}. Убедитесь, что индекс в пределах списка")


# Шаг 3
def safe_divide(a, b):
    """Функция для безопасного деления с блоком finally"""
    try:
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        print("Завершение safe_divide")


# Шаг 4
def complex_operation(a, b, c):
    """Функция с несколькими обработчиками исключений"""
    try:
        if a < 0:
            raise InvalidValueError("Число 'a' не должно быть отрицательным")
        result = a / b
        if result < c:
            raise DivisionByNegativeError("Результат меньше значения 'c'")
        return result
    except InvalidValueError as e:
        print(f"Ошибка значения: {e}")
    except DivisionByNegativeError as e:
        print(f"Ошибка деления: {e}")
    except ZeroDivisionError as e:
        print(f"Деление на ноль: {e}")
    finally:
        print("Завершение complex_operation")


# Шаг 5
def process_data(data):
    """Функция для обработки данных с генерацией исключений"""
    try:
        if not isinstance(data, dict):
            raise TypeError("Ожидается словарь")
        if "key" not in data:
            raise KeyError("Ключ 'key' отсутствует")
        if data["key"] < 0:
            raise InvalidValueError("Значение 'key' не должно быть отрицательным")
        return data["key"] * 2
    except TypeError as e:
        print(f"Тип данных не соответствует: {e}")
    except KeyError as e:
        print(f"Ошибка ключа: {e}")
    except InvalidValueError as e:
        print(f"Недопустимое значение: {e}")
    finally:
        print("Завершение process_data")


# Шаг 7
def find_resource(resources, resource_name):
    """Функция для поиска ресурса, выбрасывает исключение ResourceNotFoundError"""
    try:
        if resource_name not in resources:
            raise ResourceNotFoundError(f"Ресурс '{resource_name}' не найден")
        return resources[resource_name]
    except ResourceNotFoundError as e:
        print(f"Ошибка поиска: {e}")
    finally:
        print("Завершение find_resource")


# Шаг 8 - Примеры функций, демонстрирующие работу исключений
def open_file(filename):
    """Открытие файла с обработкой ошибок"""
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Файл не найден")
    except IOError:
        print("Ошибка ввода-вывода")
    finally:
        print("Завершение open_file")


def calculate_square_root(value):
    """Вычисление квадратного корня с проверкой значений"""
    if value < 0:
        raise InvalidValueError("Значение должно быть неотрицательным")
    return value ** 0.5


def add_positive(a, b):
    """Сложение положительных чисел, выбрасывает исключение для отрицательных значений"""
    if a < 0 or b < 0:
        raise InvalidValueError("Числа должны быть положительными")
    return a + b
