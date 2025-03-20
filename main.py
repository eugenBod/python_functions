def max_number(a, b):
    if a >= b:
        return a
    else:
        return b


def empty_function():
    pass


def even_numbers(n):
    for numbers in range(0, n + 1, 2):
        yield numbers


def test_max_number():
    assert max_number(5, 8) == 8, "Ошибка: число 8 больше числа 5"
    assert max_number(-3, -7) == -3, "Ошибка: число -3 больше числа -7"
    assert max_number(4, 4) == 4, "Ошибка: числа равны, так что без разницы какое из них выводить"
    print("Тесты пройдены")


max_number_result = max_number(34, 46)
print(f"Наибольшее число в паре: {max_number_result}")

print("Четные числа:")
for even_numbers_result in even_numbers(13):
    print(even_numbers_result)

test_max_number()
