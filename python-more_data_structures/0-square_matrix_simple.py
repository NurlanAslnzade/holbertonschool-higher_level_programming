#!/user/bin/python3

def square_matrix_simple(matrix=[]):
    a = matrix
    for i in matrix:
        for k in range(0,len(i)):
            i[k] = i[k]**2
    print(matrix)
    print(a)
