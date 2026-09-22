import numpy as np 

def matrix_multiply_numpy(a, b):
    arr_a = np.array(a)
    arr_b = np.array(b)
    return arr_a.dot(arr_b)

def matrix_multiply(a,b):
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b[0])):
                result[i][j] += a[i][k] * b[k][j]
    return result

if __name__ == "__main__":
    print(matrix_multiply([[1,2],[3,4]], [[2,0],[1,2]]))
