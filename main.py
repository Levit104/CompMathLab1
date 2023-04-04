from console import get_mode, get_size, get_accuracy, get_matrix
from iteration_method import print_results

while True:
    try:
        print('\nЧтобы выйти из программы введите "exit" на этапе выбора любого режима')
        print('\nРежимы ввода:\n\t1 - клавиатура\n\t2 - файл')

        user_input = get_mode('размерность матрицы')
        if user_input == 'exit':
            break
        else:
            size = get_size(user_input)

        user_input = get_mode('точность')
        if user_input == 'exit':
            break
        else:
            accuracy = get_accuracy(user_input)

        user_input = get_mode('элементы матрицы')
        if user_input == 'exit':
            break
        else:
            matrix = get_matrix(user_input, size)

        print_results(matrix, accuracy, size)

    except (EOFError, KeyboardInterrupt):
        print("\nВыход из программы")
        break
