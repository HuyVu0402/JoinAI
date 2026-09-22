def matrix_add(a, b):
    if len(a) != len(b):
        raise ValueError("error length")
    result = [[0] * len(a[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[i][j] = a[i][j] + b[i][j]
    return result

if __name__ == "__main__":
    print(matrix_add([[1,2],[3,4]], [[4,3],[2,1]]))
