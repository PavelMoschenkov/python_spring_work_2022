# Найти сумму элементов матрицы,
# Написать msum(matrix)  которая подсчитывает сумму всех элементов функцию Найти сумму всех элементов матрицы:
#
# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)
# 21
#
# >>> msum(load_matrix('matrix.txt'))
# 423

def msum(matrix):
    return sum([i for row in matrix for i in row])
print(f'Сумма элементов матрицы msum: {msum([[1, 2, 3], [4, 5, 6]])}')


def load_matrix(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        return [list(map(int, row.split())) for row in f.readlines()]
print(f'Сумма элементов матрицы load_matrix: {msum(load_matrix("matrix.txt"))}')