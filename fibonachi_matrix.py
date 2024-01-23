def fib_matrix(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        matrix = [[1, 1],
                  [1, 0]]
        result_matrix = matrix_pow(matrix, -n)
        return result_matrix[1][0] if n % 2 == 0 else -result_matrix[1][0]
    matrix = [[1, 1],
              [1, 0]]
    result_matrix = matrix_pow(matrix, n - 1)

    return result_matrix[0][0]


def matrix_mult(a, b):
    return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]


def matrix_pow(matrix, power):
    pre_result = [[1, 0], [0, 1]]
    while power > 0:
        if power % 2 == 1:
            pre_result = matrix_mult(pre_result, matrix)
        matrix = matrix_mult(matrix, matrix)
        power //= 2
    return pre_result
