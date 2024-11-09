"""
Главный модуль для демонстрации работы исключений.
Запускает все функции по очереди и обрабатывает возможные исключения.
"""

from functions import (
    divide, multiply_positive, get_element_from_list,
    safe_divide, complex_operation, process_data,
    find_resource, open_file, calculate_square_root, add_positive
)


def main():
    """Запуск всех функций по очереди для демонстрации работы исключений"""
    try:
        print("Шаг 1:")
        print(divide(10, 2))
        print(multiply_positive(5, 3))

        print("\nШаг 2:")
        get_element_from_list([1, 2, 3], 5)

        print("\nШаг 3:")
        print(safe_divide(10, 0))

        print("\nШаг 4:")
        complex_operation(-1, 2, 3)

        print("\nШаг 5:")
        process_data({"key": -5})

        print("\nШаг 7:")
        resource = {"database": "Connected", "cache": "Active"}
        find_resource(resource, "url") # Не найдено
        print(find_resource(resource, "database"))

        print("\nШаг 8:")
        print(open_file("file_for_open.txt"))
        print(calculate_square_root(25))
        print(add_positive(-3, 2))
    except Exception as e:
        print(f"Необработанная ошибка: {e}")


if __name__ == "__main__":
    main()
