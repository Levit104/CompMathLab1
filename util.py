import numpy as np
import copy


def print_matrix(matrix, name):
    print(f'\n{name}:')
    print('\n'.join(['\t'.join(['{:4}'.format(val) for val in row]) for row in matrix]))


# проверка
def print_check(matrix, constant_terms, answers, size):
    print('\nПроверка решения: подстановка найденных корней в исходную систему')
    row_sum = 0
    for i in range(size):
        for j in range(size):
            row_sum += matrix[i][j] * answers[j]
        print(f'Значение ряда {i + 1}:\n\tс подставленным корнем: {row_sum}\n\tточное: {constant_terms[i]}')
        row_sum = 0


# выделение свободных членов в отдельный массив
def remove_and_get_constant_terms(matrix):
    return [row.pop(-1) for row in matrix]


# проверка есть ли у матрицы диагональное преобладание
def has_diagonal_dominance(matrix, size):
    for i in range(size):
        row_sum = sum(map(abs, matrix[i][: size])) - abs(matrix[i][i])
        # row_sum = sum(abs(a[i][j]) for j in range(n) if j != i)
        if abs(matrix[i][i]) < row_sum:
            return False
    return True


# преобразование матрицы в матрицу с диагональным преобладанием
def make_diagonally_dominant(matrix, size):
    for i in range(size):
        # поиск максимального элемента в строке
        max_element = abs(matrix[i][i])
        max_row = i
        for j in range(i + 1, size):
            if abs(matrix[j][i]) > max_element:
                max_element, max_row = abs(matrix[j][i]), j
        # поменять строки, если максимальный элемент не на главной диагонали
        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]


# проверка равен ли определитель матрицы нулю
def is_singular(matrix):
    temp = copy.deepcopy(matrix)
    remove_and_get_constant_terms(temp)
    return not determinant(matrix)


def is_singular_numpy(matrix):
    temp = copy.deepcopy(matrix)
    remove_and_get_constant_terms(temp)
    return not np.linalg.det(temp)


# поиск определителя матрицы
def determinant(a):
    n = len(a)
    if n == 1:
        return a[0][0]
    elif n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    else:
        det = 0
        for i in range(n):
            det += (-1) ** i * a[0][i] * determinant(minor(a, 0, i))
        return det


# поиск минора матрицы
def minor(a, i, j):
    return [row[:j] + row[j + 1:] for row in (a[:i] + a[i + 1:])]
