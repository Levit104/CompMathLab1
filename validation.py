import os


def valid_mode(value):
    return value in ['1', '2', 'exit']


def valid_size(size):
    try:
        return 2 <= int(size) <= 20
    except ValueError:
        return False


def valid_accuracy(accuracy):
    try:
        return float(accuracy) > 0
    except ValueError:
        return False


def valid_file(path):
    return os.path.isfile(path) and os.path.getsize(path) > 0


def valid_matrix_row(row, size):
    if len(row) != size + 1:
        print('Неверное количество элементов')
        return False
    try:
        list(map(float, row))
    except ValueError:
        print('Матрица должна содержать только числа')
        return False
    return True
