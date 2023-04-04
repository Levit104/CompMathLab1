from validation import *


def get_mode(value):
    mode = input(f'\nУкажите как вводить {value}: ').strip()

    while not valid_mode(mode):
        print('Невалидный режим ввода')
        mode = input('Повторите ввод: ').strip()

    return mode


def get_file():
    path = input('Введите путь до файла: ').strip()

    while not valid_file(path):
        print('Файла не существует или он пустой')
        path = input('Повторите ввод: ').strip()

    return path


def get_one_line_from_file(path):
    with open(path, 'r') as file:
        return file.readline()


def get_size(mode):
    size = None
    if mode == '1':
        size = input('Введите размерность матрицы: ').strip()
        while not valid_size(size):
            print('Размерность матрицы невалидная: должна быть от 2 до 20')
            size = input('Повторите ввод: ').strip()
    elif mode == '2':
        size = get_one_line_from_file(get_file())
        while not valid_size(size):
            print('Размерность матрицы невалидная: должна быть от 2 до 20')
            size = get_one_line_from_file(get_file())
    return int(size)


def get_accuracy(mode):
    accuracy = None
    if mode == '1':
        accuracy = input('Введите точность: ').strip()
        while not valid_accuracy(accuracy):
            print('Точность не валидна')
            accuracy = input('Повторите ввод: ').strip()
    elif mode == '2':
        accuracy = get_one_line_from_file(get_file())
        while not valid_accuracy(accuracy):
            print('Точность не валидна')
            accuracy = get_one_line_from_file(get_file())
    return float(accuracy)


def get_matrix(mode, size):
    matrix = None
    if mode == '1':
        matrix = get_matrix_from_input(size)
    elif mode == '2':
        while not matrix:
            matrix = get_matrix_from_file(size)
    return matrix


def get_matrix_from_input(size):
    matrix = []
    print(f'Введите коэффициенты и свободные члены матрицы по рядам (в вашем случае {size + 1} эл. на ряд)\n')
    for i in range(size):
        row_id = i + 1
        # print(f'Введите элементы {row_id} ряда:')
        row = list(input().split())
        while not valid_matrix_row(row, size):
            print(f'Повторите ввод элементов {row_id} ряда:')
            row = list(input().split())
        row = list(map(float, row))
        matrix.append(row)
    return matrix


def get_matrix_from_file(size):
    path = get_file()
    matrix = []
    with open(path, 'r') as file:
        non_blank_count = 0
        for line in file:
            if line.strip() == '':
                continue
            non_blank_count += 1
            row = [val for val in line.split()]
            if not valid_matrix_row(row, size):
                return
            row = list(map(float, row))
            matrix.append(row)
        if non_blank_count != size:
            print('Неверное кол-во строк в файле')
            return
    return matrix
