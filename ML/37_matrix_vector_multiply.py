import numpy as np

def matrix_vector_multiply_numpy(matrix, vector):
    matrix_numpy = np.array(matrix)
    return matrix_numpy.dot(vector)

def matrix_vector_multiply(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise ValueError("error")
    
    result = [0] * len(matrix)
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
    return result 

if __name__ == "__main__":
    print(matrix_vector_multiply_numpy([[1,2],[3,4]], [2,1]))
