import numpy as np 

def transpose_numpy(matrix):
    return np.array(matrix).T


def transpose(matrix):
    row = len(matrix)
    col = len(matrix[0])
    result = [[0] * row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            result[j][i] = matrix[i][j]

    return result 

if __name__ == "__main__":
    print(transpose_numpy([[1,2,3],[4,5,6]]))
