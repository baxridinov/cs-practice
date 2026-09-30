a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        return None
    return x / y


print(f"Сумма: {add(a, b)}")
print(f"Разность: {sub(a, b)}")
print(f"Произведение: {mul(a, b)}")

result = div(a, b)
if result is None:
    print("Деление на ноль невозможно")
else:
    print(f"Частное: {result}")