import numpy as np


def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows, columns).tolist()


def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    arr = np.asarray(matrix, dtype=float)
    return arr[row_start:row_stop, column_start:column_stop].tolist()


def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    arr = np.asarray(matrix, dtype=float).copy()
    arr[row_start:row_stop, column_start:column_stop] = value
    return arr.tolist()


def matrix_vector_product(matrix, vector):
    a = np.asarray(matrix, dtype=float)
    v = np.asarray(vector, dtype=float)
    return (a @ v).tolist()


def matrix_multiply(left, right):
    a = np.asarray(left, dtype=float)
    b = np.asarray(right, dtype=float)
    return (a @ b).tolist()


def transpose_matrix(matrix):
    return np.asarray(matrix, dtype=float).T.tolist()


def solve_system(matrix, vector):
    a = np.asarray(matrix, dtype=float)
    b = np.asarray(vector, dtype=float)
    return np.round(np.linalg.solve(a, b), 6).tolist()


def tensor_channel_mean(tensor):
    arr = np.asarray(tensor, dtype=float)
    return arr.mean(axis=-1).tolist()


def point_distance(first, second):
    a = np.asarray(first, dtype=float)
    b = np.asarray(second, dtype=float)
    return float(round(float(np.linalg.norm(a - b)), 6))
