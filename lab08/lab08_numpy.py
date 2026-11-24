import numpy as np

print("--- Задание 1. Создание векторов и матриц ---")


hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape, "ndim:", hours.ndim, "size:", hours.size, "dtype:", hours.dtype)

print("\n--- Задание 2. Индексы и срезы в векторе ---")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("Массив в обратном порядке:", hours[::-1])

print("\n--- Задание 3. Строки и столбцы таблицы ---")
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print("Форма:", temperatures.shape, "Число измерений:", temperatures.ndim, "Число элементов:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("Центральный фрагмент 2x2:\n", temperatures[:2, 1:3])

print("\n--- Задание 4. Прямоугольные срезы ---")
matrix = np.arange(1, 26).reshape(5, 5)
print("Первые три строки:\n", matrix[:3], "\nshape:", matrix[:3].shape)
print("Последние две строки:\n", matrix[-2:], "\nshape:", matrix[-2:].shape)
print("Первые два столбца:\n", matrix[:, :2], "\nshape:", matrix[:, :2].shape)
print("Строки 1–3 и столбцы 2–4:\n", matrix[1:4, 2:5], "\nshape:", matrix[1:4, 2:5].shape)
print("Угловой блок 2x2 в правом нижнем углу:\n", matrix[-2:, -2:], "\nshape:", matrix[-2:, -2:].shape)

print("\n--- Задание 5. Изменение массива с помощью срезов ---")

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99

changed_hours[0::2] = -1
print("changed_hours:", changed_hours)
print("исходный hours:", hours)


changed_matrix = matrix.copy()
changed_matrix[1, :] = 0        # Вторая строка на нули
changed_matrix[:, -1] = -1      # Последний столбец на -1
changed_matrix[1:4, 1:4] = 100  # Центральный блок 3х3 на 100
print("changed_matrix:\n", changed_matrix)
print("исходная matrix:\n", matrix)

print("\n--- Задание 6. Изменение формы ---")
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T
print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)

