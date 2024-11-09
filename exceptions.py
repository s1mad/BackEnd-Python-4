"""
Определение пользовательских исключений для обработки ошибок в приложении.
"""

class InvalidValueError(Exception):
    """Исключение для недопустимого значения"""


class DivisionByNegativeError(Exception):
    """Исключение для деления на отрицательное число"""


class ResourceNotFoundError(Exception):
    """Исключение для случая, когда ресурс не найден"""
