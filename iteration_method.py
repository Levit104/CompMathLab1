import copy
import numpy as np
from util import print_matrix, is_singular, has_diagonal_dominance, make_diagonally_dominant, \
    remove_and_get_constant_terms, print_check


# a - матрица (со свободными членами)
# n - размер матрицы
# epsilon - точность
def solve(a, b, n, epsilon):
    iter_count = 0  # счётчик итераций
    iter_result = [0] * n  # массив для результата
    iter_measurement_error = [0] * n  # массив для погрешностей
    iter_last = [0] * n  # массив для последнего предыдущего приближения

    # в result кладем 1-ое приближения (x_0) - значения свободных членов либо 0/1
    # пример: для самого первого будет b/a_(1,1), b = a_(1,n+1)
    for i in range(n):
        iter_result[i] = b[i] / a[i][i]
        # iter_result[i] = 0
        # iter_result[i] = 1

    # кол-во итераций неизвестно => бесконечный цикл
    while True:
        # счётчик итераций + 1
        iter_count += 1

        if iter_count > 100:  # попросили так сделать, число можно взять другое
            return None, None

        # основная логика
        for i in range(n):
            # в last кладем 1-ое приближения (x_0) - на данном этапе оно равно result
            iter_last[i] = b[i] / a[i][i]
            for j in range(n):
                # пропуск "нулевого" x (если на 1-ой строке - x_1, если на 2-ой - x_2 и т.д)
                if i == j:
                    continue
                # считаем следующее приближение,
                # пример: для самого первого будет b/a_(1,1) - a_(1,2)/a_(1,1)*x_n^(k) - ... - a_(1,n)/a_(1,1)*x_n^(k)
                else:
                    iter_last[i] -= a[i][j] / a[i][i] * iter_result[j]

        # флаг для выхода из цикла, равен True если эта итерация будет последней
        final_iteration = True
        for i in range(n):
            # расчёт погрешности | x_i^(k) − x_i^(k-1) |
            iter_measurement_error[i] = abs(iter_last[i] - iter_result[i])
            # если погрешность слишком большая, то это НЕ последняя итерация, нужны ещё (флаг=False)
            if iter_measurement_error[i] > epsilon:
                final_iteration = False

        # print(f'Вектор погрешностей на {iter_count} итерации: {[round(val, 4) for val in iter_measurement_error]}')
        print(f'Вектор погрешностей на {iter_count} итерации: {iter_measurement_error}')
        # в результат кладем последнее найденное приближение
        for i in range(n):
            iter_result[i] = iter_last[i]

        # выход из while если это последняя итерация
        if final_iteration:
            break

    # возвращает массив с результатом и кол-во итераций
    return iter_result, iter_count


def print_results(matrix, accuracy, size):
    print_matrix(matrix, 'Исходная матрица')

    if is_singular(matrix):
        print('\nМатрица не имеет решения')
        return

    if not has_diagonal_dominance(matrix, size):
        print('\nМатрица не имеет диагонального преобладания')

        new_matrix = copy.deepcopy(matrix)

        make_diagonally_dominant(new_matrix, size)

        if not has_diagonal_dominance(new_matrix, size):
            print('\nНевозможно привести матрицу к диагональному преобладанию')
        else:
            matrix = new_matrix
            print_matrix(matrix, 'Преобразованная матрица')

    print()  # для красоты
    constant_terms = remove_and_get_constant_terms(matrix)
    x, count = solve(matrix, constant_terms, size, accuracy)

    if count is None:
        print('\nПревышен лимит итераций. Решение данным методом невозможно')
    else:
        print(f'\nВектор неизвестных: {x}')
        print(f'Вектор неизвестных (с округлением): {[round(val, 4) for val in x]}')
        print(f'Кол-во итераций: {count}')
        print_check(matrix, constant_terms, x, size)

    print(f'\nРешение NumPy: {np.linalg.solve(matrix, constant_terms)}')
