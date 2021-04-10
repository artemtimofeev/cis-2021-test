import copy


def minor(matrix, i, j):
    M = copy.deepcopy(matrix)
    del M[i]
    for i in range(len(matrix) - 1):
        del M[i][j]
    return M


class Matrix:
    def __init__(self, array2d):
        m = len(array2d)
        n = len(array2d[0])

        if m != n:
            raise Exception("Not square")

        self.container = array2d

    def det(self, matrix=None):
        if matrix is None:
            matrix = self.container

        m = len(matrix)
        n = len(matrix[0])

        if n == 1:
            return matrix[0][0]

        signum = 1
        determinant = 0

        # разложение по первой строке
        for j in range(n):
            determinant += matrix[0][j] * signum * self.det(minor(matrix, 0, j))
            signum *= -1

        return determinant

    def print_matrix(self):
        for strA in self.container:
            print(strA)

    def swap_on_copy(self, i_1, j_1, i_2, j_2):
        M = copy.deepcopy(self.container)

        tmp = M[i_1][j_1]
        M[i_1][j_1] = M[i_2][j_2]
        M[i_2][j_2] = tmp

        return Matrix(M)

    def swap_on_matrix(self, i_1, j_1, i_2, j_2):
        tmp = self.container[i_1][j_1]
        self.container[i_1][j_1] = self.container[i_2][j_2]
        self.container[i_2][j_2] = tmp

    def size(self):
        return len(self.container)


N = int(input())
array2d = []
for i in range(N):
    array2d.append(list(map(int, input().split())))

array2d_copy = copy.deepcopy(array2d)

Max_matrix = Matrix(array2d)

swaps = 1
while swaps > 0:
    swaps = 0

    # перебираем все a_{i, j}
    for i in range(Max_matrix.size()):
        for j in range(Max_matrix.size()):

            # перебираем все возможные перестановки для элемента a_{i, j}
            # с условием, что они уменьшают детерминант
            for i_ in range(i, Max_matrix.size()):
                for j_ in range(j, Max_matrix.size()):

                    # перестановки возможны только для элементов одной четности
                    if ((i+j) % 2) == ((i_+j_) % 2):
                        if Max_matrix.swap_on_copy(i, j, i_, j_).det() > Max_matrix.det():
                            swaps += 1
                            Max_matrix.swap_on_matrix(i, j, i_, j_)

# Максимальный детерминант:
max_det = Max_matrix.det()

# Сбрасываем до исходного, проверяем теперь минимум
Min_matrix = Matrix(array2d_copy)

swaps = 1
while swaps > 0:
    swaps = 0

    # перебираем все a_{i, j}
    for i in range(Min_matrix.size()):
        for j in range(Min_matrix.size()):

            # перебираем все возможные перестановки для элемента a_{i, j}
            # с условием, что они уменьшают детерминант
            for i_ in range(i, Min_matrix.size()):
                for j_ in range(j, Min_matrix.size()):

                    # перестановки возможны только для элементов одной четности
                    if ((i+j) % 2) == ((i_+j_) % 2):
                        if Min_matrix.swap_on_copy(i, j, i_, j_).det() < Min_matrix.det():
                            swaps += 1
                            Min_matrix.swap_on_matrix(i, j, i_, j_)

# Минимальный детерминант:
min_det = Min_matrix.det()

if -min_det > max_det:
    Min_matrix.print_matrix()
    print("max |det(M)| = ", min_det)
else:
    Max_matrix.print_matrix()
    print("max |det(M)| = ", max_det)





